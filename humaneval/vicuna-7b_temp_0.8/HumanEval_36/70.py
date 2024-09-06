

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Check for cases where n is divisible by 11 or 13.
    # If either of these cases is true, return 7 (for fizz) followed by the remainder of n/11/13.
    if n % 11 == 0 or n % 13 == 0:
        return 7 * 1 + n // 11 // 13

    # If n is not divisible by 11 or 13, check for cases where n is divisible by 11 and 7.
    # If this is true, return 7 (for fizz) followed by the remainder of n/11.
    if n % 11 == 7:
        return 7 * 1 + n // 11

    # If n is not divisible by 11 or 13 and is divisible by 11 and 7,
    # return 11 (for buzz) followed by the remainder of n/11.
    if n % 7 == 1:
        return 11 * 1 + n // 7

    # If n is not divisible by 11 or 13 and is not divisible by 11 and 7,
    # return the number of times the digit 7 appears in n (i.e., 7 is repeated).
    return 7 * n // 7
