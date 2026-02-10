import streamlit as st
from PIL import Image
from rembg import remove
import io
import requests

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Background Remover",
    page_icon="✨",
    layout="centered"
)

# ---------------- PREMIUM CSS ----------------
st.markdown("""
<style>

/* Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #000000, #111111, #000000);
    color: #f5e6c4;
    font-family: 'Segoe UI', sans-serif;
}

/* Remove header */
[data-testid="stHeader"] {
    background: transparent;
}

/* Title */
h1 {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    background: linear-gradient(90deg, #FFD700, #ffcc00, #FFD700);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 20px rgba(255, 215, 0, 0.4);
}

/* Subheadings */
h2, h3, label {
    color: #e6c76b !important;
    text-align: center;
}

/* Glass container */
.block-container {
    background: rgba(20, 20, 20, 0.7);
    padding: 2rem;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 215, 0, 0.2);
}

/* Buttons */
.stButton>button,
.stDownloadButton>button {
    background: linear-gradient(135deg, #FFD700, #c9a100);
    color: black;
    font-weight: bold;
    border-radius: 25px;
    padding: 12px 25px;
    border: none;
    transition: 0.3s ease-in-out;
}

.stButton>button:hover,
.stDownloadButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 15px rgba(255, 215, 0, 0.6);
}

/* Inputs */
.stTextInput>div>div>input,
.stTextArea textarea {
    background-color: #111111 !important;
    color: #f5e6c4 !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255, 215, 0, 0.4) !important;
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 40px;
    font-size: 18px;
    color: #c9a100;
}

.footer a {
    color: #e6c76b;
    text-decoration: none;
    font-weight: bold;
}

.footer a:hover {
    text-shadow: 0 0 10px gold;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<h2>✨ AI Background Remover</h2>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align:center;'>Remove Background in Seconds 🚀</h5>", unsafe_allow_html=True)
st.markdown("""
<div class="footer">
Developed by 
<a href="https://t.me/samyakjainbot" target="_blank"
onclick="alert('Join my Telegram Bot for more updates 🚀')">
Samyak
</a>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr style='border:1px solid rgba(255,215,0,0.3);'>", unsafe_allow_html=True)

# ---------------- IMAGE UPLOAD ----------------
uploaded_file = st.file_uploader("📤 Upload an Image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)

    st.subheader("Original Image")
    st.image(img, use_container_width=True)

    if st.button("✨ Remove Background"):
        with st.spinner("Removing background..."):
            output = remove(img)

        st.subheader("Background Removed")
        st.image(output, use_container_width=True)

        # Download
        buffer = io.BytesIO()
        output.save(buffer, format="PNG")
        buffer.seek(0)

        st.download_button(
            label="⬇ Download Image",
            data=buffer,
            file_name="background_removed.png",
            mime="image/png"
        )

# ---------------- FEEDBACK SECTION ----------------
st.markdown("<hr style='border:1px solid rgba(255,215,0,0.3);'>", unsafe_allow_html=True)
st.subheader("💬 Feedback")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    with st.form("feedback_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Write your feedback here...", height=120)

        submit = st.form_submit_button("Submit Feedback")

        if submit:
            response = requests.post(
                "https://formspree.io/f/xzdadzre",
                data={
                    "name": name,
                    "email": email,
                    "message": message
                }
            )

            if response.status_code == 200:
                st.success("Thank you for your feedback! 🚀")
            else:
                st.error("Something went wrong. Try again.")

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
Developed by 
<a href="https://t.me/samyakjainbot" target="_blank"
onclick="alert('Join my Telegram Bot for more updates 🚀')">
Samyak
</a>
</div>
""", unsafe_allow_html=True)
