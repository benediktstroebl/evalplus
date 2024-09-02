
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

    if number > 1000 or number < 1:
        raise ValueError("Number must be between 1 and 1000.")

    roman = ""

    # These variables are for storing the numbers of the given digits
    c = number // 100
    x = (number % 100) // 10
    i = number % 10

    # Iterate through the given digits, starting from the ones place.
    # If the number is 0, don't add anything to the roman numeral.
    # If the number is less than 4, add that number of characters.
    # If the number is between 4 and 9, subtract 5, and add that many characters.
    # If the number is 5, add 5 characters.
    # If the number is between 6 and 9, subtract 5, and add the 5 and that many characters.
    # If the number is 10, add the 10 characters.

    if c > 0:
        for _ in range(c):
            roman += "c"

    if x == 9:
        roman += "xc"
    elif x == 4:
        roman += "x"
    elif x > 4:
        for _ in range(x - 5):
            roman += "x"
        roman += "v"
    else:
        for _ in range(x):
            roman += "x"

    if i == 9:
        roman += "ix"
    elif i == 4:
        roman += "i"
    elif i > 4:
        for _ in range(i - 5):
            roman += "i"
        roman += "v"
    else:
        for _ in range(i):
            roman += "i"

    return roman

