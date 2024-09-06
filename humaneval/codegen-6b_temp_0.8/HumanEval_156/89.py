
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
    if not 0 < number <= 1000:
        raise ValueError('Argument must be a positive integer')

    roman_numeral = ""
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thousands = ["", "M", "MM", "MMM"]

    # Find the step to use
    while number > 0:
        step, number = divmod(number, 10)
        # Add the step
        roman_numeral += ones[step]

    # Populate the rest with the remaining number and return
    for i in range(number):
        roman_numeral += thousands[i]
    return roman_numeral

