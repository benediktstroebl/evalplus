
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
    # Convert the input number to its base-10 digits
    digits = str(number)

    # Convert the base-10 digits to their corresponding roman numerals
    numerals = []
    for digit in digits:
        numerals.append(ROMANS_MAP[digit])

    # Convert the roman numerals to the correct order
    numerals = numerals[::-1]

    # Combine the roman numerals into a single string in lowercase
    roman = ''.join(numerals)
    return roman.lower()
