
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

    roman = []
    symbol = ""
    while number > 0:
        for i in range(1, len(mini_roman_numerals)):
            if number >= mini_roman_numerals[i]:
                roman.append(symbol * mini_roman_numerals[i])
                number -= mini_roman_numerals[i]
                break
        else:
            roman.append(symbol)
            number -= 1
        symbol = mini_roman_symbols[i - 1]
    return ''.join(roman).lower()



