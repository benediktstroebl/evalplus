

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    i = 0
    for i in range(0, n):
        if i % 11 == 0 or i % 13 == 0:
            if i % 7 == 0:
                i += 3
        else:
            i += 2
    return i

list1 = list(range(1, 101))

i = 0
for x in list1:
    i += fizz_buzz(x)
