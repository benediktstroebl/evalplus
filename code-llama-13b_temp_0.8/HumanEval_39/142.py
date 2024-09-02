

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
    # corner case
    if n < 1:
        return -1

    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])

    # if the number is not prime, we need to increase n
    while not is_prime(fib[n - 1]):
        n += 1

    return fib[n - 1]

