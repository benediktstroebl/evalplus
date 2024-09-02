

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    def _fizz_buzz(n):
        # Check if n is divisible by 11 or 13
        if n % 11 == 0:
            return 0
        elif n % 13 == 0:
            return 1
        # Check if n is divisible by 111 or 113
        for i in range(2, 10):
            if n % i == 0:
                if i % 100 == 0:
                    return 1
                if i % 11 == 0:
                    return 2
                if i % 13 == 0:
                    return 3
        # If n is not divisible by any of the above, return 4
        return 4
    
    return _fizz_buzz(n)
