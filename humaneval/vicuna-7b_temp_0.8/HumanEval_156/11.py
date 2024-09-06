
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
    roman_map = {"I": "I", "V": "V", "X": "X", "L": "XL", "C": "XC", "D": "XC", "M": "CM", "H": "CM", "N": "NN", "R": "RR"}

    numeral = str(number)
    result = numeral.split('.')
    numeral = result[0] + '.' + result[1].zfill(2)

    roman_numeral = ''
    for char in numeral:
        if char.isdigit():
            char = int(char)
        elif char.isalpha():
            char = roman_map.get(char, None)
        else:
            raise ValueError(f'Invalid character {char} in {numeral}.')

        roman_numeral += char

    return roman_numeral.lower()