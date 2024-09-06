
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
        raise ValueError("Input must be between 1 and 1000 inclusive.")

    result = ""
    while number >= 1000:
        result += "m"
        number -= 1000

    if number >= 900:
        result += "cm"
        number -= 900

    while number >= 500:
        result += "d"
        number -= 500

    if number >= 400:
        result += "cd"
        number -= 400

    while number >= 100:
        result += "c"
        number -= 100

    if number >= 90:
        result += "xc"
        number -= 90

    while number >= 50:
        result += "l"
        number -= 50

    if number >= 40:
        result += "xl"
        number -= 40

    while number >= 10:
        result += "x"
        number -= 10

    if number >= 9:
        result += "ix"
        number -= 9

    while number >= 5:
        result += "v"
        number -= 5

    if number >= 4:
        result += "iv"
        
