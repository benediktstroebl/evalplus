

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

    i = 0
    curr, prev = 0, 1
    while i < n:
        curr, prev = prev, curr + prev
        if curr > n:
            return 'Please check your number.'
        for j in range(2, int(curr ** 0.5) + 1):
            if curr % j == 0:
                break
        else:
            i += 1
    return curr

