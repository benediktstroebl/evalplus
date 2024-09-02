

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
    if n < 2:
        return n

    if n == 2:
        return 2

    if n == 3:
        return 3

    prime = [2, 3]
    i = 1
    add = 4
    while i < n:
        new = prime[i] + add
        while not is_prime(new):
            new = prime[i] + add
            add += 2
        prime.append(new)

        i += 1
        add = 4

    return prime[n - 1]
