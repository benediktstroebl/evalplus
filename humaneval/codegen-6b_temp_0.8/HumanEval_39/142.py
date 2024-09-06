

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
    if n <= 0:
        return "n must be greater than 0"
    if n == 1 or n == 2:
        return n
    else:
        prev1 = 1
        prev2 = 2
        res = 1
        while n > 3:
            prev1, prev2 = prev2, prev1 + prev2
            res = prev1 + prev2
            n -= 1
        return prev1 + prev2

