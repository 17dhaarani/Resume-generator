import streamlit as st
import base64
import os

# App title
st.set_page_config(page_title="Generate your Resume", layout="wide")
st.title("Generate your Resume")
st.markdown("Create and download your personal portfolio website in minutes!")

# Sidebar Inputs
st.sidebar.header("👤 Personal Information")
name = st.sidebar.text_input("Full Name", "Dhaarani S")
title = st.sidebar.text_input("Professional Title", "Soft skills trainer, Design Thinker, Pharmaceutics educator")
email = st.sidebar.text_input("Email", "dhaarani.s.dt@snsgroups.com")
phone = st.sidebar.text_input("Phone", "8940799099")
bio = st.sidebar.text_area("Short Bio", "I am a passionate soft skills trainer, creative design thinker, and dedicated pharmaceutics educator with over 15 years of experience. I empower professionals and students through engaging workshops, fostering communication, creativity, and problem-solving, while advancing pharmaceutical education with practical, industry-relevant insights.")

st.sidebar.header("💼 Projects")
projects = []
for i in range(1, 4):
    pname = st.sidebar.text_input(f"Project {i} Name", f"Project {i}")
    pdesc = st.sidebar.text_area(f"Project {i} Description", f"This project does amazing things...")
    plink = st.sidebar.text_input(f"Project {i} Link", "https://github.com/")
    projects.append({"name": pname, "desc": pdesc, "link": plink})

st.sidebar.header("🧠 Skills")
skills = st.sidebar.text_area("Enter skills (comma-separated)", "Python, HTML, CSS, JavaScript")

st.sidebar.header("🌐 Social Links")
linkedin = st.sidebar.text_input("LinkedIn", "https://linkedin.com/in/yourname")
github = st.sidebar.text_input("GitHub", "https://github.com/yourname")
website = st.sidebar.text_input("Website/Portfolio", "https://yourportfolio.com")

# Generate HTML Portfolio
def generate_html():
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{name} - Portfolio</title>
        <style>
            body {{
                font-family: 'Segoe UI', sans-serif;
                background-color: #f9f9f9;
                margin: 0;
                padding: 20px;
                color: #333;
            }}
            .container {{
                max-width: 900px;
                margin: auto;
                background-color: white;
                padding: 30px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                border-radius: 10px;
            }}
            h1, h2 {{
                color: #007acc;
            }}
            a {{
                color: #007acc;
                text-decoration: none;
            }}
            ul {{
                padding-left: 20px;
            }}
            .section {{
                margin-bottom: 30px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{name}</h1>
            <h3>{title}</h3>
            <p><strong>Email:</strong> {email} | <strong>Phone:</strong> {phone}</p>
            <div class="section">
                <h2>About Me</h2>
                <p>{bio}</p>
            </div>
            <div class="section">
                <h2>Projects</h2>
                <ul>
    """
    for proj in projects:
        html += f"<li><strong>{proj['name']}:</strong> {proj['desc']} (<a href='{proj['link']}' target='_blank'>Link</a>)</li>"

    html += f"""
                </ul>
            </div>
            <div class="section">
                <h2>Skills</h2>
                <p>{skills}</p>
            </div>
            <div class="section">
                <h2>Social Links</h2>
                <p>
                    <a href="{linkedin}">LinkedIn</a> | 
                    <a href="{github}">GitHub</a> | 
                    <a href="{website}">Website</a>
                </p>
            </div>
        </div>
    </body>
    </html>
    """
    return html

portfolio_html = generate_html()

# Preview
st.header("📄 Live Portfolio Preview")
st.components.v1.html(portfolio_html, height=600, scrolling=True)

# Download Button
def create_download_link(content, filename):
    b64 = base64.b64encode(content.encode()).decode()
    return f'<a href="data:text/html;base64,{b64}" download="{filename}">📥 Download Portfolio</a>'

