import streamlit as st
import base64

# Resume Information
name = "Madhesh Vivekanandan"
location = "Dindigul, Tamilnadu"
email = "https://mail.google.com/mail/u/0/?ogbl#inbox?compose=DmwnWsmHbvzQnwpKRZksMrkWpMntRnNKCVGnmMTSrGmJhDfgcRtBPZhTffjxSlkqKTxLFmCwhdLv"
phone = "6374051514"
linkedin = "https://www.linkedin.com/in/madhesh-vivekanandan-3aa07a239/"
Github="https://github.com/Madheshvivekanandan"

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
    {"title": "PowerBI", "issuer": "Guvi", "date": "Mar 2024","url":"https://www.guvi.in/share-certificate/17kr6498OEv90i7V8D"},
    {"title": "Business English Certificates (BEC)", "issuer": "Cambridge University", "date": "Oct 2022","url":"unknown"},
    {"title": "NPTEL(Introduction to Programming In C)", "issuer": "Indian Institute of Technology Kanpur", "date": "Mar 2023","url":"https://nptel.ac.in/noc/E_Certificate/NPTEL23CS02S1437505103069440"},
    {"title": "Chatgpt for Everyone", "issuer": "Guvi", "date": "Apr 2024","url":"https://www.guvi.in/share-certificate/7231o978931Odzn519"},
    {"title": "Accenture North America - Data Analytics and Visualization Job Simulation", "issuer": "Forage", "date": "Mar 2024","url":"https://drive.google.com/file/d/1_psh5fNDC-oZgMxkpFFyGdgO_tJyZd7Z/view?usp=drive_link"}
]

# Publication
publication = {
    "title": "A Hybrid Crypto Trend Analysis And online Graphical Representation Model Using Neural Networks",
    "journal": "Journal of Emerging Technologies and Innovative Research",
    "date": "Mar-2024",
    "url":"http://www.jetir.org/view?paper=JETIR2403757"
}

# Streamlit Page Configuration
st.set_page_config(page_title="Resume - Madhesh Vivekanandan", layout="wide")
col1, col2,col3 = st.columns([2,2,2])
with col2:
    st.title(name)

col1, col2,col3 = st.columns([1.2,2,1])
with col2:
    # Title and Contact Information
    st.write(f"{location} · [madheshvivekanandan@gmail.com]({email}) · {phone} · [LinkedIn]({linkedin}) · [Github]({Github})")
col1, col2,col3 = st.columns([3,0.5,3])
with col1:
    # Education Section
    st.header("Education",divider="rainbow")
    for edu in education:
        st.subheader(f"[{edu["institution"]}]({edu['url']})")
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
        st.subheader(f"[{project["title"]}]({project['link']})")
        st.write(f"Technologies: {project['technologies']}")

col1, col2,col3 = st.columns([3,1,3])
with col1:
    # Certifications Section
    st.header("Certifications",divider="rainbow")
    for cert in certifications:
        col1,c, col2 = st.columns([3,1, 1])
        with col1:
            st.subheader(f"[{cert["title"]}]({cert['url']})")
            st.write(f"Issuer: {cert['issuer']}")
        with col2:
            st.write(f"{cert['date']}")
with col3:        

    # Publication Section
    st.header("Publication",divider="rainbow")
    st.subheader(f"[{publication["title"]}]({publication['url']})")
    st.write(f"Journal: {publication['journal']}")
    st.write(f"Date: {publication['date']}")

    # Skills Section
    st.header("Skills",divider="rainbow")
    for skill, details in skills.items():
        st.write(f"**{skill}**: {details}")

# # Download Resume as PDF
# resume_file_path = "/mnt/data/resume.pdf"
# with open(resume_file_path, "rb") as f:
#     pdf_data = f.read()

# b64_pdf = base64.b64encode(pdf_data).decode("utf-8")

# st.download_button(
#     label="Download Resume as PDF",
#     data=f"data:application/octet-stream;base64,{b64_pdf}",
#     file_name="Madhesh_Vivekanandan_Resume.pdf",
#     mime="application/octet-stream"
# )
