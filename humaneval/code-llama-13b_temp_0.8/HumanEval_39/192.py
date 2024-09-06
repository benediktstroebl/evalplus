

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
        return None
    prime = [True for _ in range(10000001)]
    prime[0] = prime[1] = False
    for i in range(2, 10000000):
        if prime[i]:
            for j in range(2 * i, 10000001, i):
                prime[j] = False

    phi = [1, 1]
    for i in range(2, 10000001):
        phi.append(phi[-1] + phi[-2])

    for i in range(10000000, -1, -1):
        if prime[i] and phi[i] >= n:
            return i

