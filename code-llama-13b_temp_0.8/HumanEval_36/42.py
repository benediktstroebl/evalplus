

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    if n <= 1000:
        return 0
    count = 0
    for num in range(11, n, 11):
        if num % 13 == 0 and str(num).__contains__("7"):
            count += 1
        if num % 11 == 0 and str(num).__contains__("7"):
            count += 1

    return count
