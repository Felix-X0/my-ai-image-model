async function generate() {
    const prompt = document.getElementById('prompt').value;
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = "Sedang berimajinasi...";

    try {
        const response = await fetch("https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0", {
            method: "POST",
            headers: { "Authorization": "Bearer TOKEN_ANDA_DISINI", "Content-Type": "application/json" },
            body: JSON.stringify({ inputs: prompt }),
        });
        const blob = await response.blob();
        resultDiv.innerHTML = `<img src="${URL.createObjectURL(blob)}" style="width:100%; border-radius:20px;">`;
    } catch (e) {
        resultDiv.innerHTML = "Gagal membuat gambar.";
    }
}
