import sys


def is_bulky(width: float, height: float, length: float) -> bool:
    volume = width * height * length
    return (
        volume >= 1000000 or (width >= 150 or height >= 150 or length >= 150)
    )

def is_heavy(mass: float) -> bool:
    return mass >= 20

def sort(width: float, height: float, length: float, mass: float) -> str:
    # I chose to use a separate function for each condition
    # instead of doing it inline to make the code more testable and maintainable.
    bulky = is_bulky(width, height, length)
    heavy = is_heavy(mass)

    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

def main():
    # Example usage, uncomment to use
    # width, height, length = 1, 5.2, 12.5
    # mass = 25.0
    try:
        width = float(input("Enter the width of the package: "))
        height = float(input("Enter the height of the package: "))
        length = float(input("Enter the length of the package: "))
        mass = float(input("Enter the mass of the package: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    result = sort(width, height, length, mass)
    print(f"The package is classified as: {result}")
    return result

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Goodbye!")
        sys.exit(0)
