

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

    fib_n = [0, 1]

    for i in range(2, n):
        fib_n.append(fib_n[-2] + fib_n[-1])

        is_prime = True
        for j in range(2, (fib_n[i] + 1) // 2 + 1):
            if fib_n[i] % j == 0:
                is_prime = False
                break

        if is_prime:
            return fib_n[-1]

