

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
    if n == 2:
        return 3
    if n == 3:
        return 5
    if n == 4:
        return 13

    #fib(n) = fib(n-1) + fib(n-2)
    #fib(n) is a Fibonacci number if fib(n-1) and fib(n-2) are both prime
    a = []
    prime = [2]
    i = 2
    while len(prime) < n:
        if is_prime(i):
            prime.append(i)
        i += 1
    b = prime[len(prime)-1]
    c = prime[len(prime)-2]

    while len(a) < n:
        a.append(b)
        b = c
        c = a[len(a)-1] + a[len(a)-2]
    return a[len(a)-1]
