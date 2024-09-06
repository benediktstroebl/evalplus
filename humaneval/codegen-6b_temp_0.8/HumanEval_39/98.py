

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
    if n <= 1:
        return n
    F = [0,1]
    for i in range(2,n+1):
        F.append(F[i-1]+F[i-2])
        if is_prime(F[i]):
            nth_prime = i

    return F[n]

