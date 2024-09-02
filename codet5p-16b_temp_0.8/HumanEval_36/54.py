

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """

    fizzes = 0
    buzzes = 0
    for i in range(1, n):
        if (i % 11 == 0 or i % 13 == 0) and '7' in str(i):
            fizzes += 1
            buzzes += 1
        elif i % 11 == 0 and '7' in str(i):
            fizzes += 1
        elif i % 13 == 0 and '7' in str(i):
            buzzes += 1
    return fizzes + buzzes
