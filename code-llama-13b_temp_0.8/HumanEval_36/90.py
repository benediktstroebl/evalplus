

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """

    divisible_by_11 = n//11
    count = 0
    for i in range(divisible_by_11):
        if '7' in str(i*11):
            count+=1
    return count
