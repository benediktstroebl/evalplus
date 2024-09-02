
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
    # Convert the number to its corresponding digit string
    digits = str(number)

    # Remove leading zeroes, if any
    while digits.startswith('0'):
        digits = digits[1:]

    # Convert each digit to its corresponding roman numeral
    roman_numeral = ''
    for i, digit in enumerate(digits):
        if i % 2 == 0:
            # For even digits, add the letters 'DD' or 'II' to the end
            roman_numeral += 'DD' if digit == '0' else 'II'
        else:
            # For odd digits, add the appropriate letter to the end
            roman_numeral += digit - 48 + 49

    return roman_numeral
