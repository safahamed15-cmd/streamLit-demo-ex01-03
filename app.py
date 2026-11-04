import streamlit as st

# ── Ex 01 · Headings and display ──────────────────────────────
st.title("🎓 Student Profile Card")
st.subheader("Fill in your details and generate your card")
st.markdown("---")

# ── Ex 02 · Markdown and message boxes ────────────────────────
st.markdown("""
### 📋 How this works
- Fill in every field below
- Tick the checkbox when you are ready
- Click **Generate Card** to see your profile
""")
st.info("All fields are required to generate your card.")

# ── Ex 03 · Widgets ───────────────────────────────────────────
name = st.text_input("Full Name")
age = st.slider("Age", 17, 60, 20)
major = st.selectbox("Major", ["AI", "Computer Science", "Engineering", "Mathematics"])
gpa = st.number_input("GPA (out of 4.0)", 0.0, 4.0, 3.0, step=0.1)
hobby = st.radio("Favourite hobby", ["Reading", "Coding", "Sports", "Art"])
bio = st.text_area("Short bio (2–3 sentences)")
ready = st.checkbox("I am ready to generate my card")

# ── Reaction ──────────────────────────────────────────────────
if st.button("Generate Card 🪪"):
    if not ready:
        st.warning("Please tick the checkbox first.")
    elif not name.strip():
        st.error("Please enter your name.")
    else:
        st.success(f"✅ Card generated for **{name}**!")
        st.markdown(f"""
| Field | Value |
|--------|-------|
| Name | {name} |
| Age | {age} |
| Major | {major} |
| GPA | {gpa:.1f} / 4.0 |
| Hobby | {hobby} |

> *{bio}*
""")
        st.code(f'st.write("Hello, {name}!")', language="python")
