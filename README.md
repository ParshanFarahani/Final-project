# 🚀 Space Explorer Toolkit 🌌
#### Video Demo:  [https://youtu.be/lICcy1Bw6Ww](https://youtu.be/lICcy1Bw6Ww)
#### Description:
Space Explorer Toolkit is a command-line Python application that lets users explore planetary physics and facts in an interactive, educational way. Designed for students, space enthusiasts, and educators, the toolkit includes the following features:

- 🌍 BMI Calculator: Computes BMI using Earth-based weight and height.
- 🪐 Weight on Planets: Calculates effective weight on other planets using gravity ratios.
- 🚀 Escape Velocity: Computes escape velocity using the formula √(2GM/R).
- 📊 Planetary Facts: Displays day length and year duration for selected planets.

This project demonstrates programming concepts like gravitational physics, unit conversion, error handling, and more, while introducing users to scientific applications through Python.

---

#### Installation and Running Steps:

1. Install required dependencies:
    Ensure you have Python installed. Then, install any required libraries by running:

    pip install -r requirements.txt

2. Run the application:
    Execute the Python script:

    python project.py

    Follow the on-screen prompts to explore the toolkit's features interactively.

3. Run Tests:
    To ensure the application is functioning correctly, run the tests provided in test_project.py:

    pytest test_project.py

    This will execute all test cases and verify the correctness of the implemented features.

## Tests Included

### 1. test_calculate_bmi
- Purpose: Verifies the functionality of the calculate_bmi function.
- Valid Cases:
  - Computes BMI for a valid weight and height.
- Invalid Cases:
  - Raises ValueError for zero height.
  - Raises ValueError for negative weight or height.

### 2. test_weight_on_planet
- Purpose: Verifies the functionality of the weight_on_planet function.
- Valid Cases:
  - Computes the correct weight on Mercury.
  - Computes the correct weight on Jupiter.
- Invalid Cases:
  - Raises ValueError for non-existent planet names (e.g., "Krypton").
  - Raises ValueError for negative weight.

### 3. test_escape_velocity_ms
- Purpose: Verifies the functionality of the escape_velocity_ms function.
- Valid Cases:
  - Computes the escape velocity for Earth within an acceptable range (~11,186 m/s).
- Invalid Cases:
  - Raises ValueError for unknown planets.

### 4. test_planet_facts
- Purpose: Verifies the functionality of the planet_facts function.
- Valid Cases:
  - Retrieves the correct day length (24 hours) and year duration (365.25 days) for Earth.
- Invalid Cases:
  - Raises ValueError for non-existent planets.
