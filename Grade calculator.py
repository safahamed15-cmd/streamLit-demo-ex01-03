import streamlit as st


SCALES = {
    "Standard (90 / 80 / 70 / 60)": ((90, "A"), (80, "B"), (70, "C"), (60, "D"), (0, "F")),
    "Alternative (85 / 75 / 65 / 50)": ((85, "A"), (75, "B"), (65, "C"), (50, "D"), (0, "F")),
}


def letter_grade(score, scale):
    return next(letter for minimum, letter in SCALES[scale] if score >= minimum)


st.set_page_config(page_title="Grade Garden | Grade Calculator", page_icon="🌱", layout="centered")
st.markdown("# 🌱 Grade Garden\n### Four subjects. One clear result.\nEnter your scores and see where you stand.")
st.info("Each subject contributes **25%** of your overall grade. Enter scores from 0 to 100.")

# Five input widget types: text_input, number_input, radio, checkbox, button.
name = st.text_input("Student name (optional)", max_chars=60, placeholder="Your first name")
st.markdown("### 1 · Enter your scores")
subjects = ("Mathematics", "Science", "English", "Computer Studies")
scores = []
columns = st.columns(2)
for index, subject in enumerate(subjects):
    with columns[index % 2]:
        scores.append(st.number_input(subject, min_value=0.0, max_value=100.0,
                                      value=0.0, step=0.5, format="%.1f", key=subject))

st.markdown("### 2 · Choose a grading scale")
scale = st.radio("Grading scale", options=list(SCALES))
with st.expander("How the grading works"):
    st.markdown("**The average is the sum of all four scores divided by four.**\n\n"
                "- Standard: A ≥ 90, B ≥ 80, C ≥ 70, D ≥ 60, F < 60.\n"
                "- Alternative: A ≥ 85, B ≥ 75, C ≥ 65, D ≥ 50, F < 50.\n\n"
                "These are example scales; select the one your course uses. "
                "Grades use the unrounded average. All four scores, including zeros, count.")
show_breakdown = st.checkbox("Show subject breakdown", value=True)

if st.button("Calculate", type="primary", use_container_width=True):
    average = sum(scores) / 4
    grade = letter_grade(average, scale)
    st.session_state.result = {
        "inputs": (name, tuple(scores), scale), "average": average, "grade": grade,
    }

result = st.session_state.get("result")
if result:
    if result["inputs"] != (name, tuple(scores), scale):
        st.warning("Your inputs changed. Click Calculate to update your result.")
    else:
        st.markdown("### Your result")
        greeting = f"{name.strip()}, your" if name.strip() else "Your"
        message = f"{greeting} overall letter grade is **{result['grade']}**."
        if result["grade"] in ("A", "B"):
            st.success(message)
        elif result["grade"] in ("C", "D"):
            st.warning(message)
        else:
            st.error(message + " Review the subject breakdown to plan your next steps.")
        st.metric("Average score", f"{result['average']:.2f}%")
        st.caption("Displayed average is rounded to two decimals; grading uses the exact average.")
        if show_breakdown:
            st.table([{"Subject": subject, "Score / 100": score,
                       "Letter grade": letter_grade(score, scale)}
                      for subject, score in zip(subjects, scores)])

st.divider()
st.caption("Grade Garden · A simple study companion")
