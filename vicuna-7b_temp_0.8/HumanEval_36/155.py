

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # code below this line is just a helper function
    # to check if a given number is divisible by 11 or 13
    def is_fizz_buzz(n):
        return n % 11 == 0 or n % 13 == 0

    # use recursion to traverse the numbers less than n
    # and call fizz_buzz on the numbers that are divisible by 11 or 13
    return sum(fizz_buzz(i) for i in range(n) if is_fizz_buzz(i))