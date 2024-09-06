
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
    roman_map = {
        'I': 'M',
        'V': 'X',
        'X': 'C',
        'L': 'D',
        'C': 'XC'
    }

    if number == 1:
        return 'I'
    elif number == 2:
        return 'II'
    elif number == 3:
        return 'III'
    elif number == 4:
        return 'IV'
    elif number == 5:
        return 'V'
    elif number == 6:
        return 'VI'
    elif number == 7:
        return 'VII'
    elif number == 8:
        return 'VIII'
    elif number == 9:
        return 'IX'

    result = []
    while number > 0:
        digit = number % 10
        number = number // 10
        result.insert(0, roman_map[str(digit)] if digit >= '0' and digit <= '9' else 'R')
    result.reverse()
    return ''.join(result)
