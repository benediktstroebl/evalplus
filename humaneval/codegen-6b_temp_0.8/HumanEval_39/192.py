

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
    fib = [1, 2]

    while fib[-1] < n:
        current_fib = fib[-1] + fib[-2]
        if is_prime(current_fib):
            fib.append(current_fib)

    return fib[-1]
