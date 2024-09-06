

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

    a = [1, 1]
    if n <= 2:
        return n
    else:
        for i in range(3, n + 1):
            a.append((a[i - 2] + a[i - 1]) % 10)
            if a[i] > 1:
                for j in range(2, a[i]):
                    if a[i] % j == 0:
                        break
                else:
                    return a[i]
    return a[n]

