

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # The first digit is the largest possible digit that is divisible by 11 and 13
    # We can use this digit to check if the number is divisible by 11, 13, or both.
    # If it is divisible by 13, we check if the next digit is divisible by 7.
    # If it is divisible by 11, we check if the next digit is divisible by 11 or 7.
    # If it is divisible by 7, we check if the next digit is divisible by 7.
    # Otherwise, we check if the number is divisible by 7.
    # If the number is divisible by 7, we return it.
    # Otherwise, we return 0.
    return 7 * (n // 13 if n % 13 == 1 else (n // 11 if n % 11 == 1 else n) // 7 if n % 7 == 1 else n)