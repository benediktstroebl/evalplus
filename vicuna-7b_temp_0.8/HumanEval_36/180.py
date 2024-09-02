

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Count the number of times the number appears in the range of n-1
    result = []
    for i in range(n-1, 0, -1 if n % 11 == 1 else 1):
        if n % i == 1:
            result.append(i)
        elif n % i == 0:
            result.append(i)
    # Count the number of times 7 appears in the range of n
    for i in range(len(result)):
        if n % result[i] == 0:
            result.insert(i+1, 7)
    return result