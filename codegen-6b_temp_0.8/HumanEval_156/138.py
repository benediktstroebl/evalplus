
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
    if not isinstance(number, int) or number < 1 or number > 1000:
        raise ValueError("Requires integer in range 1 to 1000")
    numerals = ["", "", "", "", "", "", "", "", "", "", "", "",
                "", "", "", "", "", "", "", ""]
    roman_numeral_map = {"M": 1000, "D": 500, "C": 100, "L": 50,
                         "X": 10, "V": 5, "I": 1}
    # Recursively build up the Roman numeral
    while number > 0:
        for i in range(10, 0, -1):
            if number - roman_numeral_map[str(i)] >= 0:
                numerals[i] = numerals[i] + "I"
                number -= roman_numeral_map[str(i)]
                break
    return "".join(numerals).lower()

