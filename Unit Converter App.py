import streamlit as st

# ── Ex 01 · Headings ──────────────────────────────────────────
st.title("🔄 Unit Converter")
st.subheader("Convert between common units instantly")
st.markdown("---")

# ── Ex 02 · Info box and markdown ────────────────────────────
st.info("Choose a category, enter a value, and see the result below.")
st.markdown("""
**Supported conversions**
- 🌡 Temperature — Celsius ↔ Fahrenheit ↔ Kelvin
- ⚖ Weight — Kilograms ↔ Pounds ↔ Ounces
- 📏 Length — Metres ↔ Feet ↔ Inches
""")

# ── Ex 03 · Widgets ───────────────────────────────────────────
category = st.radio("Category", ["Temperature", "Weight", "Length"])
value = st.number_input("Enter value", value=0.0, step=0.1)

if category == "Temperature":
    unit = st.selectbox("Convert from", ["Celsius", "Fahrenheit", "Kelvin"])
elif category == "Weight":
    unit = st.selectbox("Convert from", ["Kilograms", "Pounds", "Ounces"])
else:
    unit = st.selectbox("Convert from", ["Metres", "Feet", "Inches"])

show_formula = st.checkbox("Show the formula")

# ── Reaction ──────────────────────────────────────────────────
if st.button("Convert ⚡"):
    result = ""
    formula = ""

    if category == "Temperature":
        if unit == "Celsius":
            f = value * 9/5 + 32
            k = value + 273.15
            result = f"{value} °C = **{f:.2f} °F** = **{k:.2f} K**"
            formula = "°F = °C × 9/5 + 32 | K = °C + 273.15"
        elif unit == "Fahrenheit":
            c = (value - 32) * 5/9
            k = c + 273.15
            result = f"{value} °F = **{c:.2f} °C** = **{k:.2f} K**"
            formula = "°C = (°F − 32) × 5/9"
        else:
            c = value - 273.15
            result = f"{value} K = **{c:.2f} °C** = **{c * 9/5 + 32:.2f} °F**"
            formula = "°C = K − 273.15"

    elif category == "Weight":
        if unit == "Kilograms":
            result = f"{value} kg = **{value * 2.205:.3f} lb** = **{value * 35.274:.2f} oz**"
            formula = "lb = kg × 2.205 | oz = kg × 35.274"
        elif unit == "Pounds":
            result = f"{value} lb = **{value / 2.205:.3f} kg** = **{value * 16:.2f} oz**"
            formula = "kg = lb / 2.205 | oz = lb × 16"
        else:
            result = f"{value} oz = **{value / 35.274:.4f} kg** = **{value / 16:.4f} lb**"
            formula = "kg = oz / 35.274"

    else:
        if unit == "Metres":
            result = f"{value} m = **{value * 3.281:.3f} ft** = **{value * 39.37:.2f} in**"
            formula = "ft = m × 3.281 | in = m × 39.37"
        elif unit == "Feet":
            result = f"{value} ft = **{value / 3.281:.4f} m** = **{value * 12:.2f} in**"
            formula = "m = ft / 3.281 | in = ft × 12"
        else:
            result = f"{value} in = **{value / 39.37:.4f} m** = **{value / 12:.4f} ft**"
            formula = "m = in / 39.37"

    st.success(f"✅ {result}")
    if show_formula:
        st.markdown(f"**Formula:** {formula}")
        st.code(formula, language="text")
