
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
    rom_dict = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C',
                1000: 'M', 4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}

    digits = [int(i) for i in str(number)]

    rom_str = ''

    for digit in digits:
        if digit in rom_dict.keys():
            rom_str += rom_dict[digit]
        else:
            rom_str += rom_dict[digit]

    return rom_str

