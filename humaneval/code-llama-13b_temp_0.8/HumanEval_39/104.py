

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

    primes = [2]
    n_th_prime = [0, 1]
    cur = 1
    while primes[-1] < 10000000:
        cur = primes[-1] + primes[-2]
        if is_prime(cur):
            primes.append(cur)
            n_th_prime.append(n_th_prime[-1] + 1)
        else:
            n_th_prime.append(n_th_prime[-1])
    return primes[n_th_prime[n]]

