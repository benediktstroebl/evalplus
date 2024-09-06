

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
    if n == 0:
        return 0
    elif n == 1:
        return 2
    elif n == 2:
        return 3

    count = 3
    fib = 0
    prime = [2, 3]
    while fib < 4:
        count += 1
        fib = prime[-1] + prime[-2]
        is_prime = True
        for p in prime:
            if fib % p == 0:
                is_prime = False
                break
        if is_prime:
            prime.append(fib)
        if len(prime) >= n:
            break
    return prime[-1]

