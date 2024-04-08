function validateInput() {
  var secretKey = document.getElementById("secretKey").value;
    var keyLength = parseInt(document.getElementById("keyLength").value);
    var plainFile = document.getElementById("plainFile").value;

  // Kiểm tra xem Secret Key có được nhập hay không
  if (secretKey === "") {
    document.getElementById("error-message").innerHTML =
      "Bạn chưa nhập khóa bí mật";
    document.getElementById("error-message").style.display = "block";
    document.getElementById("error-message").style.color = "red";
    return false;
  }

  // Kiểm tra xem Length of Key có hợp lệ hay không (128, 192, hoặc 256)
  if (![128, 192, 256].includes(keyLength)) {
    document.getElementById("error-message").innerHTML =
      "Độ dài của khóa sai";
    document.getElementById("error-message").style.display = "block";
    document.getElementById("error-message").style.color = "red";
    return false;
  }

  // Độ dài của Secret Key được tính bằng số lượng ký tự
  var secretKeyLength = secretKey.length * 8; // Đổi sang số bit

  // Kiểm tra xem độ dài của Secret Key có tương ứng với Length of Key hay không
  if (secretKeyLength !== keyLength) {
    document.getElementById("error-message").innerHTML =
      "Độ dài của khóa bí mật không phù hợp với độ dài khóa";
    document.getElementById("error-message").style.display = "block";
    document.getElementById("error-message").style.color = "red";
    return false;
    }
    
    //kiểm tra xem file có được chọn hay không
    if(plainFile === ""){
        document.getElementById("error-file").innerHTML =
            "Bạn chưa chọn file";
        document.getElementById("error-file").style.display = "block";
        document.getElementById("error-file").style.color = "red";
        return false;
    }
  return true;
}
