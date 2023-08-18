document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("upload-form");
    const fileInput = document.getElementById("file-input");
    const resultDiv = document.getElementById("result");
    const imageContainer = document.getElementById("image-container");

    form.addEventListener("submit", function (e) {
        e.preventDefault();

        const formData = new FormData();
        formData.append("file", fileInput.files[0]);

        fetch("/upload", {
            method: "POST",
            body: formData,
        })
            .then(response => response.json())
            .then(data => {
                resultDiv.textContent = `Predicted Fruit: ${data.fruit}`;

                // Display uploaded image
                const imageElement = document.createElement("img");
                imageElement.src = URL.createObjectURL(fileInput.files[0]);
                imageElement.style.maxWidth = "100%";
                imageContainer.innerHTML = "";
                imageContainer.appendChild(imageElement);
            })
            .catch(error => {
                resultDiv.textContent = "Error occurred. Please try again.";
            });
    });
});