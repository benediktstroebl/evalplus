

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    for i in range(n):
        if n % 11 == 0 or n % 13 == 0:
            print(n)
            return
    print(n)

fizz_buzz(100)  # should print 0 1 2 3 4 5 7 9 11 13 15 16 17 19 20 22 23 24 26 27 28 30 31 32 34 35 36 37 38 39 40 41 42 43 45 46 47 48 49 50