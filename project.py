from math import sqrt
from typing import Tuple, Dict

#Gravitational constant for escape velocity (m^3 kg^-1 s^-2)
G = 6.67430e-11

PLANETS: Dict[str, Dict[str, float]] = {
    "Mercury": {"g_ratio": 0.38, "mass": 3.3011e23, "radius_m": 2439.7e3,
"day_hours": 1407.5, "year_days": 87.97},
    "Earth":    {"g_ratio": 1.00, "mass": 5.972e24,  "radius_m": 6371.0e3,
"day_hours": 24.0,    "year_days": 365.25},
    "Jupiter": {"g_ratio": 2.34, "mass": 1.898e27,   "radius_m": 69911e3,
"day_hours": 9.9,     "year_days": 4332.59},
 }

def list_planets() -> Tuple[str, ...]:
     """Return supportes planet names in a stable order."""

     return tuple(PLANETS.keys())

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Return BMI on Earth (kg/m^2)."""
    #validate inputes
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("weight and height must be > 0")
    # compute BMI
    return weight_kg / (height_m ** 2)

def weight_on_planet(weight_kg: float, planet: str) -> float:
    """"
    Return effective weight on a given planet using its gravity ratio.
    """
    if weight_kg <= 0:
        raise ValueError("weight must be > 0")
    name = planet.strip().capitalize()
    data = PLANETS.get(name)
    if data is None:
        raise ValueError(f"Unknown planet: {planet}")
    return weight_kg * data["g_ratio"]

def escape_velocity_ms(planet: str) -> float:
    """
    Return escape velocity for a planet in m/s using sqrt(2 * G * M / R).
    """
    name = planet.strip().capitalize()
    data = PLANETS.get(name)
    if data is None:
       raise ValueError(f"Unknown planet: {planet}")
    M = float(data["mass"])
    R = float(data["radius_m"])
    return sqrt(2 * G * M / R)

def planet_facts(planet: str) -> Tuple[float, float]:
    """
    Return float(data["day_hours"]), float(data["year_days"]) for a planet as floats.
    """
    name = planet.strip().capitalize()
    data = PLANETS.get(name)
    if data is None:
        raise ValueError(f"Unknown planet: {planet}")
    return float(data["day_hours"]), float(data["year_days"])


def _prompt_float(msg: str) -> float:
    while True:
        try:
            return float(input(msg).strip())
        except ValueError:
            print("Invalid number, try again")


def _prompt_planet() -> str:
    print("Planets:", ", ".join(list_planets()))
    return input("choose a planet: ").strip().capitalize()



def main() -> None:
    print("=== Space Explorer Toolkit (Starter) ===")
    print("This is starter code. Implement the TODOs to make tests pass.")
    print("Menu:")
    print("  1) bmi")
    print("  2) weight")
    print("  3) escape")
    print("  4) facts")
    print("  q) quit")
    choice = input("> ").strip().lower()

    try:
        if choice in ("1", "bmi"):
            weight = _prompt_float("Enter your weight in kg: ")
            height = _prompt_float("Enter your height in meters: ")
            bmi = calculate_bmi(weight, height)
            print(f"Your Earth BMI is {bmi:.2f}")

        elif choice in ("2", "weight"):
            weight = _prompt_float("Enter your Earth weight in kg: ")
            planet = _prompt_planet()
            w = weight_on_planet(weight, planet)
            print(f"On {planet}, your effective weight is {w:.2f} kg")

        elif choice in ("3", "escape"):
            planet = _prompt_planet()
            ev = escape_velocity_ms(planet)
            print(f"Escape velocity on {planet}: {ev:.0f} m/s {ev/1000:.2f} km/s")

        elif choice in ("4", "facts"):
            planet = _prompt_planet()
            day_h, year_d = planet_facts(planet)
            print(f"{planet} day length: {day_h} hours")
            print(f"{planet} year length: {year_d} Earth days")

        elif choice == "q":
            print("Bye!")
        else:
            print("Unknown choice.")
    except Exception as e:

        #Keep beginner-friendly behavior while TODOs are incomplete
        print(e)


if __name__ == "__main__":
    main()
