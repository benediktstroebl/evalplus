
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

    # Dictionaries mapping integer to roman numeral
    int_to_rom = {1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000:'m'}
    rom_to_int = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500,'m': 1000}
    rom_to_int_2 = {'iv': 4, 'ix': 9, 'xl': 40, 'xc': 90, 'cd': 400, 'cm': 900}

    def get_val(roman_numeral, int_to_rom):
        val = 0
        for ch in roman_numeral:
            val += int_to_rom[ch]
        return val

    def get_roman(number):
        if number < 4:
            return int_to_rom
