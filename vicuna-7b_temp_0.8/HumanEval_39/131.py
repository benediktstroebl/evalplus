

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    # Check if n is prime
    if not n % 1:
        return n

    # Check if n is the first Fibonacci number
    if n <= 1:
        return n

    # Check if n is the second Fibonacci number
    if n <= 2:
        return n

    # Check if n is the third Fibonacci number
    if n <= 3:
        return n

    # Check if n is the fourth Fibonacci number
    if n <= 5:
        return n

    # Check if n is the fifth Fibonacci number
    if n <= 8:
        return n

    # Check if n is the sixth Fibonacci number
    if n <= 13:
        return n

    # Check if n is the seventh Fibonacci number
    if n <= 21:
        return n

    # Check if n is the eighth Fibonacci number
    if n <= 34:
        return n

    # Check if n is the ninth Fibonacci number
    if n <= 55:
        return n

    # Check if n is the tenth Fibonacci number
    if n <= 89:
        return n

    # Check if n is the eleventh Fibonacci number
    if n <= 144:
        return n

    # Check if n is the twelfth Fibonacci number
    if n <= 233:
        return n

    # Check if n is the thirteenth Fibonacci number
    if n <= 396:
        return n

    # Check if n is the fourteenth Fibonacci number
    if n <= 718:
        return n

    # Check if n is the fifteenth Fibonacci number
    if n <= 1431:
        return n

    # Check if n is the sixteenth Fibonacci number
    if n <= 2863:
        return n

    # Check if n is the seventeenth Fibonacci number
    if n <= 5729:
