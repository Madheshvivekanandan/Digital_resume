import streamlit as st
import requests


# Resume Information
name = "Madhesh Vivekanandan"
location = "Dindigul, Tamilnadu"
email = "https://mail.google.com/mail/u/0/?ogbl#inbox?compose=DmwnWsmHbvzQnwpKRZksMrkWpMntRnNKCVGnmMTSrGmJhDfgcRtBPZhTffjxSlkqKTxLFmCwhdLv"
phone = "6374051514"
linkedin = "https://www.linkedin.com/in/madhesh-vivekanandan-3aa07a239/"
Github="https://github.com/Madheshvivekanandan"

About="To secure an entry-level engineering position in a dynamic and innovative organization where I can apply my strong academic background, technical skills, and passion for problem-solving. As a recent graduate in [Engineering field], I am eager to contribute my theoretical knowledge and practical experience gained through internships and projects. I aim to work collaboratively with a team of professionals to design, develop, and optimize solutions that address real-world challenges while continuously learning and growing in a challenging work environment."

# Education Information
education = [
    {
        "institution": "Guvi,Channai",
        "degree": "IITM Advanced Programming Professional and Master Data Science",
        "dates": "March 2024 - May 2024",
        "url":"https://www.guvi.in/"
    },
    {
        "institution": "Sri Ramakrishna Institute of Technology,Coimbatore",
        "degree": "Bachelor of Engineering Computer Science and Engineering",
        "gpa": "79.4",
        "dates": "Nov 2020 - May 2024",
        "url":"https://www.srit.org/"
    },
    {
        "institution": "Agaram Public School,Dharapuram",
        "degree": "Class 12th (CBSE)",
        "gpa": "70%",
        "dates": "June 2019 - May 2020",
        "url":"https://www.agarampublicschool.in/"
    },
    {
        "institution": "Agaram Public School,Dharapuram",
        "degree": "Class 10th (CBSE)",
        "gpa": "69%",
        "dates": "June 2017 - May 2018",
        "url":"https://www.agarampublicschool.in/"
    }
]

# Skills
skills = {
    "Programming Languages": "Python(Pandas, Streamlit, Plotly, Numpy), C",
    "SQL": "Mysql",
    "Data Visualization Tool": "Power BI",
    "Technical skills": "Data Analytics, Machine learning, Deep Learning",
    "Soft Skills": "Problem Solving, Perfectionist, Creative"
}

# Projects
projects = [
    {
        "title": "YouTube Data Harvesting and Warehousing using SQL and Streamlit",
        "technologies": "Python, Streamlit, Mysql",
        "link": "https://github.com/Madheshvivekanandan/YouTube-Data-Harvesting"
    },
    {
        "title": "Phonepe Pulse Data Visualization and Exploration",
        "technologies": "Python, Pandas, Plotly, Streamlit, Mysql",
        "link": "https://github.com/Madheshvivekanandan/Phonepe-Pulse-Data-Visualization-and-Exploration"
    },
    {
        "title": "Airbnb Analysis",
        "technologies": "Python, Data Preprocessing, PowerBI",
        "link": "https://github.com/Madheshvivekanandan/Airbnb-Analysis"
    },
    {
        "title": "Industrial Copper Modeling",
        "technologies": "Python, Machine learning, EDA, Streamlit",
        "link": "https://github.com/Madheshvivekanandan/Industrial-Copper-Modeling"
    },
    {
        "title": "Singapore Resale Flat Prices Prediction",
        "technologies": "Machine learning, ML Model Deployment, Python",
        "link": "https://github.com/Madheshvivekanandan/Singapore-Resale-Flat-Prices-Predicting"
    }
]

# Certifications
certifications = [
    {"title": "PowerBI", "issuer": "Guvi", "date": "Mar 2024","url":"https://drive.google.com/file/d/1U2fEO9J8v9NSFsCxdZKAilpiLzL9Ypxg/view?usp=drive_link"},
    {"title": "Business English Certificates (BEC)", "issuer": "Cambridge University", "date": "Oct 2022","url":"https://drive.google.com/file/d/1xeSDwWQblwOMJyVa2kGPpduaPcwaKggl/view?usp=drive_link"},
    {"title": "NPTEL(Introduction to Programming In C)", "issuer": "Indian Institute of Technology Kanpur", "date": "Mar 2023","url":"https://drive.google.com/file/d/1uXht9sX1iYx-N2oJRtCe9rsnmLXDhOg6/view?usp=drive_link"},
    {"title": "Chatgpt for Everyone", "issuer": "Guvi", "date": "Apr 2024","url":"https://drive.google.com/file/d/1jApjggJFZAP-FwmE7JViXSM7XTmk5umU/view?usp=drive_link"},
    {"title": "Accenture North America - Data Analytics and Visualization Job Simulation", "issuer": "Forage", "date": "Mar 2024","url":"https://drive.google.com/file/d/1_psh5fNDC-oZgMxkpFFyGdgO_tJyZd7Z/view?usp=drive_link"}
]

# Publication
publication = {
    "title": "A Hybrid Crypto Trend Analysis And online Graphical Representation Model Using Neural Networks",
    "journal": "Journal of Emerging Technologies and Innovative Research",
    "date": "Mar-2024",
    "url":"http://www.jetir.org/view?paper=JETIR2403757"
}
# Resume File
resume_file="https://drive.google.com/file/d/1AKwizFvyWuAC179-DAjq8z82bBJlGGLw/view?usp=sharing"
pdf_url = "https://drive.google.com/uc?export=download&id=1AKwizFvyWuAC179-DAjq8z82bBJlGGLw"

# Streamlit Page Configuration
st.set_page_config(page_title="Resume - Madhesh Vivekanandan", layout="wide")
# Fetch the PDF content
response = requests.get(pdf_url)
pdf_data = response.content

st.download_button(
        label="Download Resume PDF",
        data=pdf_data,
        file_name="your_file.pdf",
        mime="application/pdf"
    )
st.write("Note: The text in blue color are hyperlinks. If clicked, they will redirect to their respective sites/pages")
col1, col2,col3 = st.columns([2,2,2])
with col2:
    st.title(name)

col1, col2,col3 = st.columns([1.2,2,1])
with col2:
    # Title and Contact Information
    st.write(f"{location} · [madheshvivekanandan@gmail.com]({email}) · {phone} · [LinkedIn]({linkedin}) · [Github]({Github})")
st.header("About",divider="rainbow")
st.write(About)
col1, col2,col3 = st.columns([3,0.5,3])
with col1:
    # Education Section
    st.header("Education",divider="rainbow")
    for edu in education:
        e=edu["institution"]
        st.subheader(f"[{e}]({edu['url']})")
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**{edu['degree']}**")
        with col2:
            st.write(f"{edu['dates']}")
        if "gpa" in edu:
            st.write(f"GPA: {edu['gpa']}")
with col3:        
    # Projects Section
    st.header("Projects",divider="rainbow")
    for project in projects:
        p=project["title"]
        st.subheader(f"[{p}]({project['link']})")
        st.write(f"Technologies: {project['technologies']}")

col1, col2,col3 = st.columns([3,0.5,3])
with col1:
    # Certifications Section
    st.header("Certifications",divider="rainbow")
    for cert in certifications:
        col1,c, col2 = st.columns([3,1, 1])
        with col1:
            c=cert["title"]
            st.subheader(f"[{c}]({cert['url']})")
            st.write(f"Issuer: {cert['issuer']}")
        with col2:
            st.write(f"{cert['date']}")
with col3:        

    # Publication Section
    st.header("Publication",divider="rainbow")
    pu=publication["title"]
    st.subheader(f"[{pu}]({publication['url']})")
    st.write(f"Journal: {publication['journal']}")
    st.write(f"Date: {publication['date']}")

    # Skills Section
    st.header("Skills",divider="rainbow")
    for skill, details in skills.items():
        st.write(f"**{skill}**: {details}")
