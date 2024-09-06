

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
    # We start with 3, 5, 8 because these are the first numbers that are Fibonacci and prime
    # we know that all prime numbers can be expressed as 6n+1 or 6n-1
    a, b, c = 3, 5, 8
    prime_list = [2, 3, 5, 8]
    if n == 1:
        return prime_list[0]
    if n == 2:
        return prime_list[1]
    if n == 3:
        return prime_list[2]
    if n == 4:
        return prime_list[3]

    while True:
        a, b, c = b, c, b + c
        if is_prime(c) and is_fib(c):
            prime_list.append(c)
            if len(prime_list) == n:
                return prime_list[n-1]

