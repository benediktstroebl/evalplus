
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
    roman_numerals = [
        ['i', 1],
        ['v', 5],
        ['x', 10],
        ['l', 50],
        ['c', 100],
        ['d', 500],
        ['m', 1000],
    ]
    roman = ''
    current_numerals = []
    for r, n in roman_numerals:
        while number >= n:
            current_numerals.append(n)
            number -= n
    for i, n in enumerate(current_numerals):
        if i > 0 and current_numerals[i-1] >= n:
            roman += r
        elif current_numerals[i-1] < n:
            roman += r.replace('c', 'd').replace('x', 'l').replace('v', 'i')
        else:
            roman += r
    return roman

