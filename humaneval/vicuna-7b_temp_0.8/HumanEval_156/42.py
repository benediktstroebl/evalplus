
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
    # convert the number to its digits as a string
    # use a list to store the individual digits and convert them to lowercase
    digits = str(number).split()
    lowercase_digits = [chr(ord(d) - 32) for d in digits]
    # concatenate the individual digits to form the roman numeral
    roman_numeral = ''.join(lowercase_digits)
    return roman_numeral.lower()
