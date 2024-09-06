

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
        raise ValueError("n should be greater than zero")

    primes = [True] * 5000001
    prime_list = []
    primes[0] = False
    primes[1] = False
    for i in range(2, 5000001):
        if primes[i]:
            prime_list.append(i)
            for j in range(i * i, 5000001, i):
                primes[j] = False

    f = [0] * 5000001
    f[0] = 0
    f[1] = 1
    for i in range(2, 5000001):
        f[i] = f[i - 1] + f[i - 2]

    p = 0
    for i in range(0, 5000001):
        if f[i] >= prime_list[p]:
            if is_prime(f[i], prime_list, p):
                if n == 1:
                    return f[i]
                n -= 1
            p += 1

