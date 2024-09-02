

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
    res = []
    # Fibonacci series
    for i in range(n):
        if i == 0:
            res.append(2)
            continue
        elif i == 1:
            res.append(3)
            continue
        res.append(res[i - 1] + res[i - 2])
    # prime check
    for i in range(n):
        for j in range(2, int(res[i] ** 0.5) + 1):
            if res[i] % j == 0:
                break
        else:
            return res[i]

