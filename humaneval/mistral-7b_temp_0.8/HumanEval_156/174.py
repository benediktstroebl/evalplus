
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
    roman_numeral = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman = ""
    m_len = len(roman_numeral)
    while number >= 1000:
        roman += "M"
        number -= 1000
    while number >= 100:
        roman += "C"
        number -= 100
    while number >= 10:
        if number >= 90:
            roman += "XC"
            number -= 90
        elif number >= 50:
            roman += "L"
            number -= 50
        elif number >= 10:
            roman += "X"
            number -= 10
    while number >= 5:
        if number >= 9:
            roman += "IX"
            number -= 9
        elif number >= 4:
            roman += "IV"
            number -= 
