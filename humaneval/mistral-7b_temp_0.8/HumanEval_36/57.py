

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # DIVIDE NUMBERS BY 11 OR 13 AND COUNT OCCURENCES OF THE DIGIT 7
    count = 0
    for n in range(2, n + 1):
        if n % 11 == 0 or n % 13 == 0:
            count += ''.join(map(str, n)).count('7')
    return count

