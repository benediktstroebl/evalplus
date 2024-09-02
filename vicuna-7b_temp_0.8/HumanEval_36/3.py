

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # For the base case, n is less than 10, return the number of times 7 appears in the numbers 1-n.
    if n < 10:
        return sum(1 for i in range(1, n+1) if i % 11 == 0 or i % 13 == 0)
    else:
        # Otherwise, n is greater than or equal to 10, so we need to loop through the numbers 1-n and check if they are divisible by 11 or 13.
        return sum(1 for i in range(1, n+1) if i % 11 == 0 or i % 13 == 0)
