

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    d = {3: 'Fizz', 5: 'Buzz', 7: '7'}
    res = 0
    for i in range(1, n):
        if str(i).count('7') != 0:
            res += str(i).count('7')
        if i % 11 == 0 or i % 13 == 0:
            res += str(i).count('7')
    return res
