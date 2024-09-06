
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
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    number_chars = []
    remainder = 0
    current_digit = 1000
    while number != 0:
        digit = number % 1000
        number /= 1000
        number_chars.append(digit)
        value = remainder * 100 + digit
        remainder = value // 100
        current_digit = roman_map.get(str(value % 100))
        if current_digit:
            number_chars.append(current_digit)
        else:
            number_chars.append('0' * (4 - len(str(value % 100))))
        if remainder == 0:
            break
    return ''.join(reversed(number_chars))
