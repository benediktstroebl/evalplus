
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """

    # Assuming uppercase I is a placeholder
    # Converting the given integer to string for ease of manipulation
    integer_to_roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    number = str(number).upper()
    # Find the index of 4th and 5th characters of the string
    fourth = number[3]
    fifth = number[4]

    # Determining the subtractions
    if fourth == "I":
        if fifth == "I":
            return number[:3] + "C" + number[4:]
        else:
            return number[:3] + "X" + number[4:]

    # Removing lowercase I's
    elif fourth == "V":
        return number[:3] + "V" + number[4:]
    elif fourth == "X":
        return number[:3] + "X" + number[4:]

    # Determining additions
    elif fifth == "I":
        if fourth == "L":
            return number[:3] + "X" + number[4:]
        elif fourth == "D":
            return number[:3] + "C" + number[4:]
        elif fourth == "M":
            return number[:3] + "M" + number[4:]

    return number

