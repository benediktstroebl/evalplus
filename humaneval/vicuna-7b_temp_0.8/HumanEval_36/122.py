

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Check the first three numbers
    if n % 11 == 0:
        return 0
    elif n % 13 == 0:
        return 0
    else:
        # Calculate the number of 7's, 11's and 13's in the number
        num7 = 0
        num11 = 0
        num13 = 0
        for i in range(n):
            if n % 7 == 0:
                num7 += 1
            elif n % 11 == 0:
                num11 += 1
            elif n % 13 == 0:
                num13 += 1
        # Return the number of 7's and 11's
        return num7 + num11