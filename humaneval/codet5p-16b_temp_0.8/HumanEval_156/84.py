
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

    if type(number)!= int:
        raise TypeError('Given argument is not an integer')

    if not 0 < number <= 1000:
        raise ValueError('Given argument is not between 1 and 1000')

    roman_dict = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }
    num_symbols = []
    for symbol in roman_dict:
        while roman_dict[symbol] <= number:
            num_symbols.append(symbol)
            number -= roman_dict[symbol]
    return ''.join(num_symbols).lower()
