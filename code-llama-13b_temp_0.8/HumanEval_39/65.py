

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
    # To get the n-th number that is a Fibonacci number
    # we start at 0th number
    i = 0

    # We start the sequence with 0 and 1.
    a = 0
    b = 1

    # a will represent the n-th Fibonacci number
    while i != n:
        c = a + b
        a = b
        b = c
        i += 1

    # To check if the number is prime we just need to check if it's divisible by any number between 2 and sqrt(n)
    while 2 < b:
        if b % 2 != 0:
            break
        b = b / 2
    # If the number is not divisible by any number between 2 and sqrt(n) then it's prime
    if b != 1:
        return False
    # Otherwise we return the number
    return a

