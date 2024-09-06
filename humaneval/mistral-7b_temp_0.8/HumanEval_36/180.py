

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # To prevent checking for 7 in n, the value for n must be greater than 7.
    # The value of n must be greater than 13 to prevent checking for 7 in n mod 13.
    if n < 13:
        return 0
    else:
        count = 0
        for i in range(n):
            if i % 11 == 0 or i % 13 == 0:
                if i % 7 == 0:
                    count += 1
    return count

