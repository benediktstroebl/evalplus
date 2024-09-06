

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
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        if len(fib_seq) > 1000:
            return None
        if all(fib_seq[i - 1] % j != 0 for j in range(2, fib_seq[i - 1]**0.5 + 1)):
            continue
        else:
            fib_seq = fib_seq[:-1]
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[-1]

