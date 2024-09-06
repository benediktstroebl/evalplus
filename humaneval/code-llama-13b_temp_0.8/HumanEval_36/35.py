

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # If the number is not divisible by either 11 or 13 then return 0
    if n % 11 != 0 and n % 13 != 0:
        return 0

    count = 0
    # Iterate over a list of strings to represent the numbers from 1 to n
    for i in [str(i) for i in range(1, n)]:
        if "7" in i:
            count += 1
    return count

