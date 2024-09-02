

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
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        fib_list = fibonacci_sequence()
        fib_sum = 0
        idx = 0
        while fib_sum < n:
            fib_sum += fib_list[idx]
            idx += 1
        return fib_list[idx-1]
