

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
    # find all primes from 2 to n
    primes = [2]
    for num in range(3, n, 2):
        flag = 0
        for p in primes:
            if num % p == 0:
                flag = 1
                break
        if flag == 0:
            primes.append(num)

    # find all Fibonacci numbers to n
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])

    # find n-th prime Fibonacci number
    i = 0
    while i < len(fib):
        if fib[i] in primes:
            return fib[i]
        i += 1

    return -1

