
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
    mini_tens = ['', 'x', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix']
    mini_ones = ['', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix']
    
    if number < 1 or number > 1000:
        return 'Invalid'
    output = ''
    if number < 10:
        output += mini_tens[number]
    else:
        while number > 0:
            value = (number - (number % 10)) / 10
            output += mini_tens[value] + mini_ones[number % 10]
            number = value
    return output.lower()
