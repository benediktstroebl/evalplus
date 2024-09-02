

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
        raise ValueError("The number cannot be less than one")
    primes = [2, 3, 5, 7]
    index = 3
    a = 1
    b = 1
    c = a + b
    while c < 1000000:
        if c % 2 == 0 or c % 5 == 0:
            c += 1
        else:
            if is_prime(c, primes):
                primes.append(c)
                index += 1
                if index == n:
                    return c
            c += 1
    return c

