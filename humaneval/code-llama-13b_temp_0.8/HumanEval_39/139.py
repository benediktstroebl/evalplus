

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

    pfib = []  # prime fibonacci list
    fib = [1, 1]  # fibonacci list
    prime = [2, 3, 5, 7]  # prime list
    for i in range(10000):
        fib.append(fib[i] + fib[i + 1])

        if fib[i + 2] >= 100000:
            break

    # add prime numbers to the prime list
    for i in range(len(fib)):
        flag = True
        for j in range(2, int(math.sqrt(fib[i])) + 1):
            if fib[i] % j == 0:
                flag = False
        if flag:
            prime.append(fib[i])

    # add prime fibonacci numbers to the prime fibonacci list
    for i in range(len(prime)):
        flag = True
        for j in range(2, int(math.sqrt(prime[i])) + 1):
            if prime[i] % j == 0:
                flag = False
        if flag:
            pfib.append(prime[i])

    return pfib[n - 1]


