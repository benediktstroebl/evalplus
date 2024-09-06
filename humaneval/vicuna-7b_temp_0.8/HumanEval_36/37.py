

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Mark if the number is divisible by 11 or 13
    is_fizz = n % 11 == 0
    is_buzz = n % 13 == 0

    # Mark if the number is divisible by 7
    is_fizzbuzz = n % 7 == 0

    # Check if any of the conditions are met and return the number of times 7 appears
    if is_fizz and is_buzz and is_fizzbuzz:
        return 7
    elif is_fizz:
        return 11
    elif is_buzz:
        return 13
    elif is_fizzbuzz:
        return 7
    else:
        return 0
