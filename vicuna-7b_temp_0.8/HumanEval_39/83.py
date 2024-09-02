

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
    if n < 2:
        return 2
    elif n < 3:
        return 3
    elif n < 5:
        return 2, 3
    else:
        is_prime = True
        candidate = 2
        for i in range(5, int(n**0.5) + 1):
            if (candidate**2 > n) or (candidate % 2 == 0):
                is_prime = False
                break
            candidate += 2
        if is_prime:
            return candidate
        return (candidate,)
