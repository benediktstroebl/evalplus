

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

    # The Fibonacci numbers will be held in this list
    fib = [1, 2]
    i = 3  # current number under consideration
    n_found = 2  # number of Fibonacci numbers found so far

    while n_found < n:
        fib.append(fib[-1] + fib[-2])
        i += 1
        if is_prime(i):
            n_found += 1

    return fib[-1]

