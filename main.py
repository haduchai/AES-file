# from werkzeug.wrappers import Request, Response
from flask import Flask, render_template, request
from flask_cors import CORS
import timeit
import aes

def string_to_hex(input_string):
    # Khởi tạo một chuỗi rỗng để lưu kết quả
    hex_string = ""
    # Duyệt qua từng ký tự trong chuỗi đầu vào
    for char in input_string:
        # Chuyển đổi ký tự thành giá trị hexa và thêm vào chuỗi kết quả
        hex_string += format(ord(char), '02x')
    return hex_string

def hex_to_string(input_hex):
    # Khởi tạo một chuỗi rỗng để lưu kết quả
    string = ""

    # Duyệt qua từng cặp ký tự hexa trong chuỗi đầu vào
    for i in range(0, len(input_hex), 2):
        # Chuyển đổi cặp ký tự hexa thành ký tự và thêm vào chuỗi kết quả
        string += chr(int(input_hex[i:i + 2], 16))

    return string

# Khởi tạo Flask server backend
app = Flask(__name__, template_folder='templates')

# Apply flask CORS
cors = CORS(app)

# Khai báo route từ index.html
@app.route('/')
# @cross_origin()
def home():
    # Read file index.html and return
    # return open('index.html', 'r', encoding = 'UTF-8').read()
    return render_template('index.html')
    
@app.route('/home', methods=['GET', 'POST'])
# @cross_origin()
def index():
    # Lấy dữ liệu từ index.html
    secretKey = request.form['secretKey']
    secretKey = string_to_hex(secretKey)
    secretKey = bytes.fromhex(secretKey)

    start = timeit.default_timer()
    button_clicked = request.form['button']
    # print(request.form)
    # if request.form['plainFile'] != '':
    if button_clicked == 'encrypt':
        # plainText = request.form['plainText']
        file = request.files['plainFile']
        plainText = file.read().decode("utf-8")
        plainText_ = string_to_hex(plainText)
        inp = bytes.fromhex(plainText_)
        encrypted = aes.AES(secretKey).encrypt(inp)
        print('encrypt: ',encrypted.hex())
        # print(plainText)
        return render_template('index.html', secretKey = secretKey.decode('utf-8'), output = encrypted.hex(), time = timeit.default_timer() - start)
        

    # if request.form['cipherText'] != '':
    if button_clicked == 'decrypt':
        file = request.files['plainFile']
        cipherText = file.read().decode("utf-8")
        cipherText_ = bytes.fromhex(cipherText)
        decrypted = aes.AES(secretKey).decrypt(cipherText_)
        print('decrypt: ',decrypted.decode('utf-8'))
        return render_template('index.html', secretKey = secretKey.decode('utf-8'), output = decrypted.decode('utf-8'), time = timeit.default_timer() - start)
    return render_template('index.html')

# Start Backend server
if __name__ == '__main__':
    app.run(host='localhost', port='9000', debug=True)
    # from werkzeug.serving import run_simple
    # run_simple('localhost', 8999, app)