import streamlit as st
import random
import string

# Function to generate password
def generate_password(length, use_digits, use_special, exclude_chars):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_special:
        characters += string.punctuation

    # Remove excluded characters
    if exclude_chars:
        characters = ''.join([char for char in characters if char not in exclude_chars])

    return ''.join(random.choice(characters) for _ in range(length))

# Function to check password strength percentage
def check_password_strength(password):
    strength = 0
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1

    # Calculate strength percentage
    strength_percentage = (strength / 4) * 100
    return strength_percentage

# Function to get strength level and color
def get_strength_level_and_color(strength_percentage):
    if strength_percentage < 50:
        return "WEAK", "red"
    elif 50 <= strength_percentage < 70:
        return "MEDIUM", "orange"
    else:
        return "STRONG", "green"

# Streamlit App
st.title("Advanced Password Generator and Strength Checker")

# Sidebar for additional options
st.sidebar.header("Options")
num_passwords = st.sidebar.number_input("Number of Passwords to Generate", min_value=1, max_value=10, value=1)

# Password configuration
length = st.slider("Select Password Length", min_value=8, max_value=30, value=12)
use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")
exclude_chars = st.text_input("Exclude Specific Characters (e.g., @, $, etc.)", "")

# Generate passwords
if st.button("Generate Password(s)"):
    passwords = []
    for _ in range(num_passwords):
        password = generate_password(length, use_digits, use_special, exclude_chars)
        passwords.append(password)

    # Display passwords
    st.write("### Generated Password(s):")
    for i, password in enumerate(passwords, 1):
        strength_percentage = check_password_strength(password)
        level, color = get_strength_level_and_color(strength_percentage)

        st.write(f"Password {i}: `{password}`")
        st.write(f"Strength: {strength_percentage:.2f}%")
        st.markdown(
            f"<div style='background-color: {color}; padding: 10px; border-radius: 5px; text-align: center; font-weight: bold; color: white;'>{level}</div>",
            unsafe_allow_html=True,
        )
        st.write("-----------------------")

# New Feature: Check Strength of User-Provided Password
st.write("### Check Strength of Your Password")
user_password = st.text_input("Enter a password to check its strength:", type="password")

if user_password:
    strength_percentage = check_password_strength(user_password)
    level, color = get_strength_level_and_color(strength_percentage)

    st.write(f"Your Password: `{user_password}`")
    st.write(f"Strength: {strength_percentage:.2f}%")
    st.markdown(
        f"<div style='background-color: {color}; padding: 10px; border-radius: 5px; text-align: center; font-weight: bold; color: white;'>{level}</div>",
        unsafe_allow_html=True,
    )