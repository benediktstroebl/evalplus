
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

    assert 1 <= number <= 1000

    roman_numeral = ''

    for i in range(1, number + 1):
        if i == 1000:
            roman_numeral +='m'
            break
        elif i >= 100:
            if i >= 100:
                roman_numeral += 'c'
                i -= 100
            if i >= 10:
                roman_numeral += 'l'
                i -= 10
            if i >= 1:
                roman_numeral += 'x'
                i -= 1
        elif i >= 50:
            if i >= 50:
                roman_numeral += 'd'
                i -= 50
            if i >= 10:
                roman_numeral += 'v'
                i -= 10
            if i >= 1:
                roman_numeral += 'l'
                i -= 1
        elif i >= 10:
            if i >= 10:
                roman_numeral += 'x'
                i -= 10
            if i >= 1:
                roman_numeral += 'v'
                i -= 1
        elif i >= 5:
