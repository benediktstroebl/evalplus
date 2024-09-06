
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

    # Pre-make the symbols with corresponding values
    symbol_values = [
        ('i', 1),
        ('v', 5),
        ('x', 10),
        ('l', 50),
        ('c', 100),
        ('d', 500),
        ('m', 1000)
    ]

    # Turn the number into a list of numeral symbols
    num_symbols = []
    num = number
    for symbol, value in symbol_values:
        while num >= value:
            num -= value
            num_symbols.append(symbol)

    # Convert the list of symbols to a string
    return ''.join(num_symbols)

