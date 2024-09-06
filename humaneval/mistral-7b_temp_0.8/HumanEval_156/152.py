
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

    if number < 1 or number > 1000:
        raise Exception('Invalid input')

    # symbols
    symbols = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    values = [1000, 500, 100, 50, 10, 5, 1]

    result = ''
    for i in range(len(symbols)):
        # if input number is greater than value
        while number > values[i]:
            result += symbols[i]
            number -= values[i]

    return result

