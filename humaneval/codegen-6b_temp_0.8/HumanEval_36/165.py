

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    def fizzbuzz():
        for i in range(n):
            if i % 11 == 0 or i % 13 == 0:
                yield 'Fizz'
            elif i % 7 == 0:
                yield 'Buzz'
            elif i % 11 == 0:
                yield 'Fizz'
            elif i % 13 == 0:
                yield 'Fizz'
            else:
                yield i

    return sum(1 for _ in fizzbuzz())

