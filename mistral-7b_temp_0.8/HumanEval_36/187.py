

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # 11 and 13 are prime numbers, so the only way a multiple of both will be a multiple of 7 is if it's divisible by 7.
    # So we can use the same logic as "Fizz Buzz" problem, where we check if the number is divisible by 7, and then by 11 and 13.
    num_sevens = 0
    for n in range(1, n + 1):
        if n % 7 == 0 and n % 11 == 0 and n % 13 == 0:
            num_sevens += 1
    return num_sevens
