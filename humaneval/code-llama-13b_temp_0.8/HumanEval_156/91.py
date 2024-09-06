
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
    # uncomment this for testing
    # assert(1 <= number <= 1000)

    roman = ''
    multiplier = 1000
    while multiplier > 0:
        digit = number // multiplier
        if digit == 1:
            roman += 'm'
        elif digit == 2:
            roman += 'n'
        elif digit == 3:
            roman += 'o'
        elif digit == 4:
            roman += 'p'
        elif digit == 5:
            roman += 'q'
        elif digit == 6:
            roman += 'r'
        elif digit == 7:
            roman += 's'
        elif digit == 8:
            roman += 't'
        elif digit == 9:
            roman += 'u'
        elif digit == 10:
            roman += 'v'
        elif digit == 50:
            roman += 'w'
        elif digit == 100:
            roman += 'x'
        elif digit == 500:
            roman += 'y'
        elif digit == 1000:
            roman += 'z'
        else:
            if digit >= 10:
                roman += 'z' + 'o' * (digit - 10)
            elif digit >= 9:
                roman += 'o' + 'n' * (digit - 9)
            elif digit >= 8:
                roman += 'n' + 'o' * (digit - 8)
            elif digit >= 7:
                roman += 'o' + 's' * (digit - 7)
            elif digit >= 6:
                roman += 's' + 'o' * (digit - 6)
            elif digit >= 5:
                roman += 'o' + 'r' * (digit - 5)
            elif digit >= 4:
                roman += 'r' + 'o' * (digit - 4)
            elif digit >= 3:
                roman += 'o' + 't' * (digit - 3)
            elif digit >= 2:
                roman += 't' + 'o' * (digit - 
