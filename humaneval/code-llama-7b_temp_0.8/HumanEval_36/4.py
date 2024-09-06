

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    div11 = div13 = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            div11 += int(str(i).__contains__('7'))
            div13 += int(str(i).__contains__('7'))
        if i % 13 == 0:
            div11 += int(str(i).__contains__('7'))
        if i % 11 == 0:
            div13 += int(str(i).__contains__('7'))
    return div11 + div13

