
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

    # Handle easy case of 1
    if number == 1:
        return 'i'

    mini_roman = ''
    ones = ['', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix']
    tens = ['x', 'xx', 'xxx', 'xl', 'l', 'lx', 'lxx', 'lxxx', 'xc']
    thousands = ['c', 'cc', 'ccc', 'cd', 'd', 'dc', 'dcc', 'dccc', 'cm']

    # Build the roman numeral from the right
    while number > 0:
        # Get remainder of the number
        rem = number % 10
        # Find the roman numeral for the remainder
        roman = ones[rem]
        # Add it to the growing roman numeral
        mini_roman = roman + mini_roman
        # Remove the remainder from the number to be converted
        number = number // 10

    # Return the roman numeral in lowercase
    return mini_roman.lower()
