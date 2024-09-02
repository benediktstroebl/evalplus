

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    while n > 0:
        if n % 11 == 0:
            print(n, "FizzBuzz")
        elif n % 13 == 0:
            print(n, "Fizz")
        elif n % 3 == 0:
            print(n, "Buzz")
        n //= 11