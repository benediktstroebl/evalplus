
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
    roman_map = [
        'I', 'V', 'X', 'L', 'XL', 'XC', 'CD', 'D', 'C', 'CC', 'CD',
        'XXX', 'VIII', 'VII', 'VI', 'V', 'IV', 'I'
    ]
    roman_map.append('I')  # One
    roman_map.append('II')  # Two
    roman_map.append('III')  # Three
    roman_map.append('IV')  # Four
    roman_map.append('V')  # Five
    roman_map.append('VI')  # Six
    roman_map.append('VII')  # Seven
    roman_map.append('VIII')  # Eight
    roman_map.append('IX')  # Nine
    roman_map.append('X')  # Ten

    roman_map.extend(['X', 'L', 'XL', 'XC', 'CD', 'D', 'C', 'CC', 'CD'])

    i = 0
    result = ''
    while number > 0:
        if number >= 1000:
            result = roman_map[i] + result
            number -= 1000
            i += 1
            continue
        elif number >= 900:
            result = roman_map[i] + result
            number -= 900
            i += 1
            continue
        elif number >= 800:
            result = roman_map[i] + result + 'V'
            number -= 800
            i += 1
            continue
        elif number >= 700:
            result = roman_map[i] + result + 'IV'
            number -= 700
            i += 1
            continue
        elif number >= 600:
            result = roman_map[i] + result + 'III'
            number -= 600
            i += 1
            continue
        elif number >= 500:
            result = roman_map[i] + result + 'II'
            number -= 500
            i += 1
