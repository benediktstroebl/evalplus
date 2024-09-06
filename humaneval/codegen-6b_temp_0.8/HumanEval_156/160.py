
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
    if number <= 0 or number > 1000:
        raise ValueError("Please provide a positive integer between 1 and 1000.")

    # Variables
    conv = ''
    add = 0

    # Iterate through numeral
    for i in range(len(numeral)):
        # Add ten to base, if it's an integer
        add = 10 if numeral[i] == 'x' else 0
        # Add roman numeral
        conv += roman[int(number / numeral[i])]
        # Subtract seven from number, if it's a tenth
        number -= numeral[i] * add

    # Reverse the final result
    return conv[::-1]
