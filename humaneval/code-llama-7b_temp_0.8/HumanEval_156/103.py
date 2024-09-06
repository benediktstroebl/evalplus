
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

    # NOTE: There's no need to convert the string to a lowercase. The string 
    # will automatically be lowercased by the chr function
    if number < 1 or number > 1000:
        raise ValueError("The number must be between 1 and 1000")
    elif number <= 10:
        return chr(0x60 + number)
    elif number <= 100:
        return (chr(0x60 + (number // 10)) + chr(0x60 + (number % 10)))
    elif number <= 1000:
        return (chr(0x60 + (number // 100)) + 'h' + 
                chr(0x60 + ((number % 100) // 10) + (number % 10)))
    else:
        raise AssertionError("You forgot to handle a big number")


