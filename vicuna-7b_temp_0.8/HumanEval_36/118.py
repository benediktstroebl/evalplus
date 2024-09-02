

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Let's first check if n is divisible by 11 or 13
    if n % 11 == 0 or n % 13 == 0:
        return 0
    # If n is not divisible by 11 or 13, we need to check all the numbers between 1 and n-1
    for i in range(1, n+1):
        # If i is divisible by 7, we add 1 to the count of the number of 7's
        if i % 7 == 0:
            count += 1
        # If i is divisible by 3, we add the number of 7's to the count of 3's
        if i % 3 == 0:
            count += count_3s(i)
        # If i is divisible by 5, we add the number of 3's to the count of 5's
        if i % 5 == 0:
            count += count_5s(i)
    return count
