

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
    previous = 1
    current = 1
    prime_previous = True
    prime_current = True
    current_count = 2
    while current_count < n:
        current, previous = current + previous, current
        if current_count % 2 == 0:
            prime_current = is_prime(current)
        else:
            prime_previous = is_prime(previous)
        if prime_current and prime_previous:
            return current
        current_count += 1
    return None

