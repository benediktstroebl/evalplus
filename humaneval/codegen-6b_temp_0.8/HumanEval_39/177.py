

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
    f: List[int] = [2, 3]
    while len(f) < n:
        f.append(f[-1] + f[-2])
    prime: bool = is_prime(f[-1])
    while not prime:
        f.append(f[-1] + f[-2])
        prime = is_prime(f[-1])
    return f[-1]

