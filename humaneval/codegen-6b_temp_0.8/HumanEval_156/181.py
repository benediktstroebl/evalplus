
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
    # create lists of roman numerals
    digits = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    vals = [1, 5, 10, 50, 100, 500, 1000]
    rns = ''
    for i in range(len(vals)):
        while number >= vals[i]:
            rns += digits[i]
            number -= vals[i]
    return rns
