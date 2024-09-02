

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    result = []
    for i in range(n):
        if i % 11 == 0:
            result.append(fizz[i % 11])
        elif i % 13 == 0:
            result.append(buzz[i % 13])
        else:
            result.append(str(i))
    return result

for i in range(1, 101):
    print(i, fizz_buzz(i))