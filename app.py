import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(page_title='Tratamento Automático',
                    layout='wide')

with st.sidebar:
    st.image('https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png')
    st.title('Background Remover - Alpha 00')
    st.info('This app allows you remove the background of your photo!')

def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


def fix_image(upload):
    image = Image.open(upload)
    col1.write("Your photo :camera:")
    col1.image(image)
    fixed = remove(image)
    col2.write("Fixed photo :wrench:")
    col2.image(fixed)
    st.markdown("\n")
    st.download_button("Download fixed photo", convert_image(fixed), "fixed.png", "photo/png")

st.markdown('# Remove the background here')
my_upload = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

col1, col2 = st.columns(2)

if my_upload is not None:
    fix_image(my_upload)
