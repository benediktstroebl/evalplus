

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    "*** YOUR CODE HERE ***"
    i = 0
    while n >= i:
        if i % 11 == 0 or i % 13 == 0:
            i += 1
            continue
        if i % 7 == 0:
            i += 1
            print("fizz", end=" ")
        elif i % 11 == 0:
            i += 1
            print("buzz", end=" ")
        elif i % 13 == 0:
            i += 1
            print("fizz buzz", end=" ")
        else:
            i += 1
            print(i, end=" ")
    return i - 1
    
