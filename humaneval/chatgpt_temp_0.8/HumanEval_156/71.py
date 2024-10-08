def int_to_mini_roman(number):
    roman_numerals = [
        ("m", 1000),
        ("cm", 900),
        ("d", 500),
        ("cd", 400),
        ("c", 100),
        ("xc", 90),
        ("l", 50),
        ("xl", 40),
        ("x", 10),
        ("ix", 9),
        ("v", 5),
        ("iv", 4),
        ("i", 1)
    ]
    if not 1 <= number <= 1000:
        raise ValueError("Invalid input. Please provide a number between 1 and 1000.")
    result = ""
    for numeral, value in roman_numerals:
        while number >= value:
            result += numeral
            number -= value
    return result.lower()
