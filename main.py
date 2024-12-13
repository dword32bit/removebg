import streamlit as st
import cv2
import numpy as np
from PIL import Image

def remove_background(image):
    # Mengubah gambar menjadi format RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Menggunakan model untuk menghapus background
    model = cv2.createBackgroundSubtractorMOG2()
    fgMask = model.apply(image)
    
    # Mengubah gambar menjadi format RGBA
    image_rgba = cv2.cvtColor(image, cv2.COLOR_RGB2RGBA)
    image_rgba[fgMask == 0] = [0, 0, 0, 0]
    
    return image_rgba

def main():
    st.title("Hapus Background Gambar")
    st.write("Unggah gambar Anda untuk menghapus background")
    
    # Mengunggah gambar
    uploaded_file = st.file_uploader("Pilih Gambar", type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file is not None:
        # Membaca gambar
        image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
        
        # Menghapus background
        image_rgba = remove_background(image)
        
        # Menampilkan hasil
        st.image(image_rgba, channels="RGBA")
        
        # Mengunduh hasil
        pil_img = Image.fromarray(image_rgba)
        buffer = BytesIO()
        pil_img.save(buffer, format="PNG")
        st.download_button("Unduh Hasil", data=buffer.getvalue(), file_name="hasil.png")

if __name__ == "__main__":
    main()
