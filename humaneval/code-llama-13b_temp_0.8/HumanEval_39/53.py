

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
    fib = [1, 1]
    prime_index = 2
    index = 2
    while index <= n:
        num = fib[0] + fib[1]
        fib[0] = fib[1]
        fib[1] = num
        is_prime = is_prime_number(num)
        if is_prime:
            prime_index += 1
        if prime_index == index:
            index += 1
    return fib[1]

