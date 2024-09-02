

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
        return

    last_1 = 1
    last_2 = 0
    count = 0
    curr = 0
    while count <= n:
        curr = last_1 + last_2
        last_2 = last_1
        last_1 = curr
        if is_prime(curr) and is_fibo(curr):
            count += 1

    return curr

