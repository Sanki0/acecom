const imageInput = document.querySelector("#imageInput")
var uploadedImage = ""

imageInput.addEventListener("change", function() {
  const reader = new FileReader()
  reader.addEventListener("load", () => {
    uploadedImage = reader.result
    document.querySelector("#displayImage").style.backgroundImage = `url(${uploadedImage})`
  })
  reader.readAsDataURL(this.files[0])
})