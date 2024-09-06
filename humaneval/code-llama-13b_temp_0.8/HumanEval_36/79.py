

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Hint: Use for loop
    num_7s = 0
    for num in range(1, n):
        # Check if the number is divisible by 11 or 13
        if num % 11 == 0 or num % 13 == 0:
            num_str = str(num)
            # Check if the number contains the digit 7
            if "7" in num_str:
                num_7s += 1
    return num_7s


