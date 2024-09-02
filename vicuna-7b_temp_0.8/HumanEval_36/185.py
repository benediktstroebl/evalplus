

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Check for cases 1 and 2, return 0 if either of them is true
    if n % 11 == 0 or n % 13 == 0:
        return 0

    # Check for case 3
    if n % 11 == 13:
        return 1

    # Check for cases 4 to 10
    for i in range(4, 11):
        if n % i == 0:
            return i

    # Check for cases 11 to 100
    for i in range(11, 101, 11):
        # Check if n is divisible by 11
        if n % i == 0:
            # Check if the n - i is divisible by 13
            if (n - i) % 13 == 0:
                # If both conditions are true, return 3
                return 3
            # If only one condition is true, return the number of times 7 appears in n - i
            elif (n - i) % 11 == 0:
                return 1
            # If neither condition is true, return the number of times 7 appears in n - i
            else:
                return 0
        # If n is not divisible by 11, return the number of times 7 appears in n
        else:
            return 7

    # Check for cases 101 to 199
    for i in range(101, 200, 11):
        # Check if n is divisible by 11
        if n % i == 0:
            # Check if the n - i is divisible by 13
            if (n - i) % 13 == 0:
                # If both conditions are true, return 3
                return 3
            # If only one condition is true, return the number of times 7 appears in n - i
            elif (n - i) % 11 == 0:
                return 1
            # If neither condition is true, return the number of times 7 appears in n - i
            else:
                return 0
        # If n is
