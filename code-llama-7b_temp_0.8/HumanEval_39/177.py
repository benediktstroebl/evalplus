

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
    prime_list = []
    prime_list.append(2)
    prime_list.append(3)
    current = 5
    while len(prime_list) != n:
        if is_prime(current):
            prime_list.append(current)
        current += 4
    return prime_list[-1]

