

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
    if n < 1:
        raise ValueError("n must be an integer greater than 0")
    if n == 1:
        return 2
    if n == 2:
        return 3
    first, second, temp = 2, 3, 4
    while n > 2:
        last = temp
        temp = first + second
        first = second
        second = last
        n -= 1
    return last

