

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
    if n == 1:
        return 2
    elif n == 2:
        return 3
    if n % 2 == 0:
        return 4
    previous_prime, current_prime = 3, 5
    count = 3
    while count < n:
        previous_prime, current_prime = current_prime, current_prime + previous_prime
        if is_prime(current_prime):
            count += 1
    return current_prime
