
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
    numeral = str(number)
    roman_numeral = ""
    for char in numeral:
        if char in ["I", "V", "X", "L", "C", "D", "M", "N", "R"]:
            roman_numeral += char
        elif char == "0":
            if roman_numeral == "":
                roman_numeral = "0"
            else:
                roman_numeral += "0"
        else:
            break
    return roman_numeral[::-1]
