

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
    if n <= 0:
        return 0
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        if is_prime(n-1) and is_prime(n-2):
            return n-1
        else:
            for i in range(2, int(n**0.5)-1):
                if is_prime(i):
                    n = i
                    break
            return n
