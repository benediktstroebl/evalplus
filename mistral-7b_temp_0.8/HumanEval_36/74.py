

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Count the number of digits 7 in numbers less than n which are divisible by 11 or 13.
    # If the number is divisible by 11, then every digit is either 0, 1, 2, 3, 4, 5, or 7,
    # so we only need to check the last digit.
    # If the number is divisible by 13, then every digit is either 1, 3, 7, or 9,
    # so we only need to check the first digit.
    count = 0
    while n > 0:
        if n % 13 == 0:
            if n % 10 == 7:
                count += 1
        elif n % 11 == 0:
            if n % 100 == 7:
                count += 1
        n -= 1
    return count

