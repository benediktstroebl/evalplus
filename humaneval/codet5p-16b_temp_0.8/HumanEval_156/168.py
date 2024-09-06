
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

    result = ""
    roman_numerals = (('x', 'ix'), ('clii', 'c'), ('cccc', 'cd'), ('mmmm', 'cm'), ('vvvv', 'xv'), ('dddd', 'd'), ('eeee', 'ex'), ('bbbb', 'v'), ('ccc', 'xc'), ('vv', 'ixv'), ('ll', 'xl'), ('dd', 'ix'), ('nn', 'xn'), ('vvv', 'v'), ('ddd', 'd'), ('eee', 'ex'), ('bb', 'ix'), ('cc', 'x'), ('vv', 'ixv'), ('ll', 'xl'), ('dd', 'ix'), ('nn', 'xn'), ('vvv', 'v'), ('ddd', 'd'), ('eee', 'ex'), ('bbbb', 'v'), ('cccc', 'cd'), ('vvvv', 'xv'), ('mmmm', 'cm'), ('dddd', 'd'), ('eeee', 'ex'), ('ccccc', 'cc'), ('vvvvv', 'ix'), ('llll', 'xc'), ('nnnn', 'xn'), ('vv
