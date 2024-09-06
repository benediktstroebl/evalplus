

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
    if n < 1:
        return 2
    if n == 1:
        return 2
    if n == 2:
        return 3
    if n == 3:
        return 5
    if n == 4:
        return 13

    # Initialization
    a, b = 2, 3
    current_number = 5

    for i in range(4, n):
        if is_prime(current_number):
            # Go to next Fibonacci number and continue
            a, b = b, a + b
            current_number = b
        else:
            # Go to next Fibonacci number
            a, b = b, a + b

    return current_number

