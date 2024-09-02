

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Save the current time in a variable
    start = time.time()
    result = []
    for i in range(1, n+1):
        if i % 11 == 0:
            result.append(7)
        if i % 13 == 0:
            result.append(7)
        elif i % 3 == 0:
            result.append(1)
        elif i % 5 == 0:
            result.append(2)
        else:
            result.append(i)
    end = time.time()
    print(f"{n} takes {end - start} seconds")
    return result
