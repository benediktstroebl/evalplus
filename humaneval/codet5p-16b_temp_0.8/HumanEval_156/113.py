
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

    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    keys = [key for key in roman_dict.keys()]
    keys.reverse()
    roman_numeral = ""
    for i in range(0, len(keys)):
        if number >= roman_dict[keys[i]]:
            number -= roman_dict[keys[i]]
            roman_numeral += keys[i]
        if number == 0:
            return roman_numeral
        if i == len(keys) - 1:
            return "No solution"
    return roman_numeral
