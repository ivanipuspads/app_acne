import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Tentukan path model yang sudah dilatih
model_path = 'keras_model.h5'  # Ganti dengan path model yang sesuai
model = load_model(model_path)

# Tentukan ukuran gambar dan nama kelas
IMAGE_WIDTH, IMAGE_HEIGHT = 224, 224
class_names = open("labels.txt", "r").readlines()
# Fungsi untuk memprediksi gambar
def predict(image, model):
    image = image.resize((IMAGE_WIDTH, IMAGE_HEIGHT))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    prediction = model.predict(image)
    predicted_class = np.argmax(prediction, axis=1)[0]
    confidence = np.max(prediction) * 100
    return predicted_class, confidence

# Sidebar untuk navigasi
st.sidebar.title("Navigasi")
page = st.sidebar.selectbox("Pilih Halaman", ["Home", "Prediksi", "About"])

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
        color: black;
    }
    .sidebar .sidebar-content {
        background-color: #c9c9ff;
        color: black;
    }
    .stButton>button {
        background-color: #6c63ff;
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
    }
    .black-text {
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Halaman Home
if page == "Home":
    st.markdown("<h1 style='text-align: center;' class='black-text'>🌟 Selamat Datang di Aplikasi Diagnosa Acne 🌟</h1>", unsafe_allow_html=True)
    st.markdown("""
        <p class='black-text'>
        Aplikasi ini bertujuan untuk membantu mendeteksi jenis acne pada gambar yang diunggah.
        <br>Dengan menggunakan model deep learning, aplikasi ini dapat mengklasifikasikan gambar acne 
        ke dalam beberapa kategori dengan tingkat akurasi yang tinggi.
        </p>
    """, unsafe_allow_html=True)
    
    # Tambahkan gambar kelas untuk memberikan visualisasi
    st.markdown("<h2 class='black-text'>📸 Contoh Kategori Kelas</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<p class='black-text' style='text-align:center; font-size: 18px; font-weight: bold;'>Tidak Berjerawat</p>", unsafe_allow_html=True)
        image_no_acne = Image.open("image/120.jpg")  # Ganti dengan path gambar yang sesuai
        resized_image_no_acne = image_no_acne.resize((300, 300))  # Mengubah ukuran gambar
        st.image(resized_image_no_acne, caption="Contoh wajah tanpa acne", use_column_width=True)
        st.markdown("""
            <p class='black-text'>
            Ini adalah contoh wajah tanpa acne. Wajah ini memiliki kulit yang bersih tanpa adanya jerawat atau komedo.
            <br>Cara menjaga kulit tetap bersih termasuk rutin membersihkan wajah dan menjaga kebersihan kulit.
            </p>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("<p class='black-text' style='text-align:center; font-size: 18px; font-weight: bold;'>Jerawat Level 1</p>", unsafe_allow_html=True)
        image_with_acne1 = Image.open("image/levle1_7.jpg")  # Ganti dengan path gambar yang sesuai
        resized_image_with_acne1 = image_with_acne1.resize((300, 300))  # Mengubah ukuran gambar
        st.image(resized_image_with_acne1, caption="Contoh wajah dengan acne level 1", use_column_width=True)
        st.markdown("""
            <p class='black-text'>
            Ini adalah contoh wajah dengan jerawat level 1. Wajah ini memiliki jerawat kecil yang terlihat di beberapa area kulit.
            <br>Cara mencegah jerawat termasuk menjaga kebersihan kulit, menghindari kosmetik yang menyumbat pori-pori,
            dan menjaga pola makan yang sehat.
            </p>
        """, unsafe_allow_html=True)
        

    # Tambahkan contoh untuk level jerawat lainnya
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("<p class='black-text' style='text-align:center; font-size: 18px; font-weight: bold;'>Jerawat Level 2</p>", unsafe_allow_html=True)
        image_with_acne2 = Image.open("image/levle2_7.jpg")  # Ganti dengan path gambar yang sesuai
        resized_image_with_acne2 = image_with_acne2.resize((300, 300))  # Mengubah ukuran gambar
        st.image(resized_image_with_acne2, caption="Contoh wajah dengan acne level 2", use_column_width=True)
        st.markdown("""
            <p class='black-text'>
            Ini adalah contoh wajah dengan jerawat level 2. Wajah ini memiliki jerawat yang lebih besar dan lebih banyak.
            <br>Penanganan yang tepat bisa meliputi perawatan kulit yang lebih intensif dan konsultasi dengan dermatologis.
            </p>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("<p class='black-text' style='text-align:center; font-size: 18px; font-weight: bold;'>Jerawat Level 3</p>", unsafe_allow_html=True)
        image_with_acne3 = Image.open("image/levle3_0.jpg")  # Ganti dengan path gambar yang sesuai
        resized_image_with_acne3 = image_with_acne3.resize((300, 300))  # Mengubah ukuran gambar
        st.image(resized_image_with_acne3, caption="Contoh wajah dengan acne level 3", use_column_width=True)
        st.markdown("""
            <p class='black-text'>
            Ini adalah contoh wajah dengan jerawat level 3. Wajah ini memiliki jerawat yang parah dengan peradangan yang signifikan.
            <br>Perawatan medis mungkin diperlukan untuk mengelola jerawat level ini secara efektif.
            </p>
        """, unsafe_allow_html=True)
        
    st.markdown("<h2 class='black-text'>🚀 Fitur Utama</h2>", unsafe_allow_html=True)
    st.markdown("""
        <ul class='black-text'>
            <li>Mendeteksi jenis acne pada gambar wajah.</li>
            <li>Memberikan prediksi kategori acne dengan tingkat level jerawat dan akurasi.</li>
            <li>Memungkinkan pengguna untuk mengunggah gambar untuk analisis.</li>
        </ul>
    """, unsafe_allow_html=True)
    
    st.markdown("<h2 class='black-text'>📊 Tampilan Data</h2>", unsafe_allow_html=True)
    st.markdown("""
        <p class='black-text'>
        Aplikasi ini menyajikan visualisasi contoh kategori kelas acne, yaitu wajah tanpa acne dan wajah dengan acne,
        untuk memberikan gambaran kepada pengguna.
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<h2 class='black-text'>📣 Call to Action</h2>", unsafe_allow_html=True)
    st.markdown("""
        <p class='black-text'>
        Silakan gunakan tombol navigasi di sebelah kiri untuk mengakses halaman prediksi, tentang aplikasi ini, 
        atau untuk informasi lebih lanjut.
        </p>
    """, unsafe_allow_html=True)

# Halaman Prediksi
elif page == "Prediksi":
    st.markdown("<h1 class='black-text'>🔍 Prediksi Gambar Acne</h1>", unsafe_allow_html=True)
    
    st.markdown("<h2 class='black-text'>🧠 Deskripsi Model</h2>", unsafe_allow_html=True)
    st.markdown("""
        <p class='black-text'>
        Prediksi dilakukan menggunakan model deep learning yang telah dilatih menggunakan data gambar wajah 
        dengan dan tanpa acne. Model ini dapat memprediksi dengan tingkat akurasi yang tinggi berdasarkan fitur-fitur 
        yang dipelajari selama pelatihan.
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<h2 class='black-text'>🖼️ Input</h2>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Unggah gambar acne", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gambar yang diunggah", use_column_width=True)
        
        predicted_class, confidence = predict(image, model)
        
        class_description = {
            0: "Jerawat Level 1: Jerawat kecil yang terlihat di beberapa area kulit. Biasanya tidak meradang.",
            1: "Jerawat Level 2: Jerawat yang lebih besar dan lebih banyak, mungkin sedikit meradang.",
            2: "Jerawat Level 3: Jerawat yang parah dengan peradangan yang signifikan, memerlukan perawatan medis.",
            3: "Tidak Berjerawat: Kulit wajah yang bersih tanpa adanya jerawat atau komedo."
        }
        
        st.markdown(f"<p class='black-text'><strong>Prediksi Kelas:</strong> {class_names[predicted_class]}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='black-text'><strong>Akurasi:</strong> {confidence:.2f}%</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='black-text'><strong>Deskripsi:</strong> {class_description[predicted_class]}</p>", unsafe_allow_html=True)


# Halaman About
elif page == "About":
    st.markdown("<h1 class='black-text'>📝 Tentang Aplikasi Ini</h1>", unsafe_allow_html=True)
    st.markdown("""
        <h2 class='black-text'>🌟 Tentang Proyek</h2>
        <p class='black-text'>
        Aplikasi ini dibuat untuk membantu pengguna dalam mendeteksi dan mengidentifikasi jenis jerawat pada gambar wajah. 
        Jerawat adalah masalah umum yang mempengaruhi banyak orang, terutama remaja, dan dapat disebabkan oleh faktor-faktor 
        seperti perubahan hormon, pola makan, dan kebersihan kulit.
        <br><br>
        Dengan memanfaatkan teknologi deep learning menggunakan TensorFlow dan Streamlit, aplikasi ini dapat memberikan 
        prediksi yang akurat tentang apakah sebuah gambar wajah mengalami jerawat atau tidak. Pengguna dapat mengunggah 
        gambar untuk mendapatkan prediksi klasifikasi serta mengetahui tingkat kepercayaan dari prediksi tersebut.
        <br><br>
        Menjaga kebersihan kulit, menghindari penggunaan kosmetik yang menyumbat pori-pori, serta pola makan yang sehat 
        adalah beberapa langkah yang dapat membantu mencegah jerawat. Aplikasi ini diharapkan dapat memberikan kontribusi 
        dalam membantu pengguna dalam merawat dan memahami kondisi kulit mereka.
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<h2 class='black-text'>👥 Tim Pengembang</h2>", unsafe_allow_html=True)
    st.markdown("""
        <p class='black-text'>
        Aplikasi ini dikembangkan oleh tim kecil yang berfokus pada pengembangan aplikasi berbasis AI untuk kesehatan dan kecantikan.
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<h2 class='black-text'>📧 Kontak</h2>", unsafe_allow_html=True)
    st.markdown("""
        <p class='black-text'>
        Hubungi kami melalui Instagram untuk informasi lebih lanjut atau berkontribusi pada pengembangan aplikasi ini:
        <br>
        <a href="https://www.instagram.com/ivanipuspads/" target="_blank">Instagram - @ivanipuspads</a>
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<h2 class='black-text'>📚 Referensi</h2>", unsafe_allow_html=True)
    st.markdown("""
        <p class='black-text'>
        Untuk informasi lebih lanjut tentang jerawat dan teknologi deep learning:
        <br>
        - <a href="https://www.webmd.com/skin-problems-and-treatments/acne/what-is-acne" target="_blank">WebMD - What Is Acne?</a>
        <br>
        - <a href="https://www.tensorflow.org/" target="_blank">TensorFlow Official Website</a>
        <br>
        - <a href="https://streamlit.io/" target="_blank">Streamlit Official Website</a>
        </p>
    """, unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px;">
        <hr>
        <small class='black-text'>© 2024 Aplikasi Prediksi Acne. All rights reserved.</small>
    </div>
    """,
    unsafe_allow_html=True
)
