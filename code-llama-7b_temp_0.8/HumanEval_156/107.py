
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
    roman_numerals = {
        (1000, 'm'): (  ('m',  1000),   ( 'c',   100),   ( 'x',    10)),
        ( 100, 'c'): (  ('c',   100),   ( 'l',    50),   ( 'x',    10)),
        (  10, 'x'): (  ('x',    10),   ( 'v',     5),   ( 'i',    1)),
        (   1, 'i'): (  ('i',    1),    None,        None)
    }
    roman = ''
    for (base, roman_char) in roman_numerals:
        (quotient, number) = divmod(number, base)
        if quotient > 0:
            roman += (roman_char * quotient)
    return roman.lower()

