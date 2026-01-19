import streamlit as st

# Resume generator function
def generate_resume(name, role, skills, education, projects):
    resume = f"""
NAME: {name}

ROLE:
{role}

SKILLS:
{skills}

EDUCATION:
{education}

PROJECTS:
{projects}

SUMMARY:
{name} is a motivated individual aiming for a career as a {role}.
Skilled in {skills}, with academic background in {education}.
"""
    return resume


# Streamlit UI
st.set_page_config(page_title="AI Resume Generator", page_icon="📄")

st.title("📄 AI Resume Generator")
st.write("Fill the details below to generate your resume")

# Input fields
name = st.text_input("Full Name")
role = st.text_input("Role / Career Objective")

skills = st.text_area("Skills (comma separated)")
education = st.text_area("Education Details")
projects = st.text_area("Projects")

# Button
if st.button("Generate Resume"):
    if name and role and skills and education:
        resume_output = generate_resume(
            name, role, skills, education, projects
        )

        st.subheader("🧾 Generated Resume")
        st.text(resume_output)

        # Download option
        st.download_button(
            label="⬇️ Download Resume",
            data=resume_output,
            file_name="resume.txt",
            mime="text/plain"
        )
    else:
        st.warning("⚠️ Please fill all required fields")
