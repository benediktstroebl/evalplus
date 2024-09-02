
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
    if isinstance(number, int) and 0 < number <= 1000:
        numerals = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        symbols = [
            'M', 'CM', 'D', 'CD',
            'C', 'XC', 'L', 'XL',
            'X', 'IX', 'V', 'IV',
            'I'
        ]
        converted = ''
        for numeral, symbol in zip(numerals, symbols):
            converted += ((number // numeral) * symbol) if number > numeral else (symbol * (number // numeral))
            number %= numeral
        return converted.lower()
    else:
        raise ValueError('int_to_mini_roman takes a positive integer number between 1 and 1000')

