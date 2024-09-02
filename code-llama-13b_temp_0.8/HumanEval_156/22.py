
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
    thousands = ['', 'm', 'mm', 'mmm']
    hundreds = ['', 'c', 'cc', 'ccc', 'cd', 'd', 'dc', 'dcc', 'dccc', 'cm']
    tens = ['', 'x', 'xx', 'xxx', 'xl', 'l', 'lx', 'lxx', 'lxxx', 'xc']
    ones = ['', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix']
    roman_num = ''

    # Convert the integer to a string.
    number = str(number)
    # Pad the number with zeros to make it length 4.
    number = number.rjust(4, '0')
    # Split the number into its digits.
    digits = list(number)
    # Join the digits into a string.
    digits = ''.join(digits)

    # Convert the digits to roman numerals.
    # The order of the following conditions are important!
    if digits[0] == '1':
        roman_num += ones[int(digits[3])]
    else:
        roman_num += thousands[int(digits[0])]

    if digits[1] == '1':
        roman_num += tens[int(digits[2])]
    else:
        roman_num += hundreds[int(digits[1])]

    if digits[2] == '1':
        roman_num += ones[int(digits[3])]
    else:
        roman_num += tens[int(digits[2])]

    return roman_num.lower()

