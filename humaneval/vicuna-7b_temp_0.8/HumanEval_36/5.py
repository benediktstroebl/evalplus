

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Only bother computing the number of times 7 appears in multiples of 11 or 13 if the value of n is not divisible by 11 or 13
    if n % 11 or n % 13 != 0:
        # Calculate the number of times 7 appears in multiples of 11 or 13
        for i in range(1, n):
            if (i % 11) == 7:
                print(f"{i} {fizz_count(i)} {buzz_count(i)}")
        # Calculate the number of times 7 appears in the first n-1 integers that are divisible by 11 or 13
        for i in range(2, n-1):
            if (i % 11) == 7:
                print(f"{i} {fizz_count(i)} {buzz_count(i)}")
    else:
        print(n)
