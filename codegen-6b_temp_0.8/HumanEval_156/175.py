
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
    # Your code here
    if number <= 0 or number > 1000:
        raise ValueError("Number out of bounds")
    if number == 1:
        return 'i'
    s = []
    while number > 0:
        n = number % 10
        if n == 0:
            s.append('0')
            number //= 10
            continue
        if n == 4:
            s.append('iv')
            number -= 4
            continue
        if n == 5:
            s.append('v')
            number -= 5
            continue
        if n == 9:
            s.append('ix')
            number -= 9
            continue
        if n < 4:
            s.append(str(n) + 'i')
        elif n == 4:
            s.append('iv')
        elif n == 5:
            s.append('v')
        elif n == 9:
            s.append('ix')
        number //= 10
    return ''.join(reversed(s)).lower()

