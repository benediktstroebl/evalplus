
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

    num_chars = 0
    num_str = ''
    for num, roman in roman_map.items():
        while num > 0:
            num //= 1000
            num_str += roman[num % 1000]
            num_chars += 1
            if num % 1000 == 0:
                num_str += 'M'
            if num % 100 == 0:
                num_str += 'D'
            if num % 10 == 0:
                num_str += 'C'
            if num % 10 == 0:
                num_str += 'XC'
            if num % 10 == 0:
                num_str += 'L'
            if num % 10 == 0:
                num_str += 'XL'
            if num % 10 == 0:
                num_str += 'X'
            if num % 10 == 0:
                num_str += 'V'
            if num % 10 == 0:
                num_str += 'IV'
            if num % 10 == 0:
                num_str += 'I'
            num /= 100

    return num_str.lower()
