
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
    # Make a default value, so that we can avoid exceptions
    # or help the user make a mistake
    roman = ''
    if number < 1:
        return roman
    if number > 1000:
        return roman

    num_map = (
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),
    )

    # Loop while we have a valid entry
    while number > 0:
        for num, roman_num in num_map:
            if number >= num:
                number -= num
                roman += roman_num
    return roman

assert int_to_mini_roman(19) == 'xix'
assert int_to_mini_roman(152) == 'clii'
assert int_to_mini_roman(426) == 'cdxxvi'
assert int_to_mini_roman(1) == 'I'
assert int_to_mini_roman(2) == 'II'
assert int_to_mini_roman(3) == 'III'
assert int_to_mini_roman(4) == 'IV'
assert int_to_mini_roman(5) == 'V'
assert int_to_mini_roman(6) == 'VI'
assert int_to_mini_roman(7) == 'VII'
assert int_to_mini_roman(8) == 'VIII'
assert int_to_mini_roman(9) == 'IX'
assert int_to_mini_roman(10) == 'X'
assert int_to_mini_roman(20) == 'XX'
assert int_to_mini_roman(50) == 'L'
assert int_to_mini_roman(60) == 'LX'
assert int_to_mini_roman(80) == 'LXX'
assert int_to_mini_roman