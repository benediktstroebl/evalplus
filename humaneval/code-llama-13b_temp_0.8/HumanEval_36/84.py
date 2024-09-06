

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # "cheat" and use another function that was provided in the exercise
    from fizz_buzz_help import divisible_by
    
    count = 0
    for i in range(1, n):
        if divisible_by(i, 11) or divisible_by(i, 13):
            if "7" in str(i):
                count += 1
    return count
