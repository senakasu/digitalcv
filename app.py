from pathlib import Path

import streamlit as st
from PIL import Image

#--- Profile maker https://pfpmaker.com/
#--- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir/"styles"/"main.css"
resume_file = current_dir/"assets"/"cv.pdf"
profile_pic = current_dir/"assets"/"profile-pic.png"

#--- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Senaka Suriyaarachchi"
PAGE_ICON = ":wave:"
NAME = "Senaka Suriyaarachchi"
DESCRIPTION = """
Senior Full Stack Java Developer, having skills in Angular ,Python, Steamsit, Oracle and Java.
"""

EMAIL = "senakas@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com",
    "Github": "https:/github.com",
}

PROJECTS = {
    "CWW Lite",
    "Service Circle",
}
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
#--- LOAD CSS. PDF & PROFILE PIC
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

#--- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write(":email:", EMAIL)

#--- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

#--- EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
    - 10 + Years experience in application development
    - Strong hands on experience and knowledge in Java and SQL databases (Oracle, MariaDB, Informix)
    - Experience in Full Stack development with Angular, Ionic, Python
    - Good knowledge in Data visualization using Plotly dash and Streamlit

    """
)

#--- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

#--- JOB 1
st.write(":wave:", "**Senior Developer | Care Systems Inc**")
st.write("01/05/2018 - Present")
st.write(
    """
        Used Java, Angular, Python to develop business applications.
    """
)




