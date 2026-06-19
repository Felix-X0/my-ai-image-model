import torch
from diffusers import StableDiffusionPipeline

# 1. Load model dari Hugging Face
# Kita gunakan model dasar yang ringan untuk demonstrasi
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(
    model_id, 
    torch_dtype=torch.float16
)

# Pindahkan ke GPU (wajib untuk AI gambar)
pipe = pipe.to("cuda")

def generate_nft(prompt_text):
    """
    Fungsi utama untuk membuat gambar berdasarkan deskripsi teks.
    """
    print(f"Sedang memproses: {prompt_text}...")
    
    # Menjalankan AI
    image = pipe(prompt_text).images[0]
    
    # Simpan hasil
    output_filename = "nft_result.png"
    image.save(output_filename)
    
    return output_filename

# Contoh pemanggilan skrip
if __name__ == "__main__":
    prompt = "Dark fantasy anime character, katana, ethereal lighting, high detail, 8k"
    result = generate_nft(prompt)
    print(f"Gambar berhasil dibuat: {result}")
