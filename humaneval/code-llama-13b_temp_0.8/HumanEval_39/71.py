

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
    # check if n is in the first 2 Fibonacci numbers
    if n < 2:
        return n + 1

    # initialise variables
    fib1: int = 0
    fib2: int = 1
    # counter for prime Fibonacci numbers
    p_fib_counter: int = 1

    # loop until we find n-th prime Fibonacci number
    while p_fib_counter < n:
        # calculate next Fibonacci number
        fib_next: int = fib1 + fib2
        # update variables
        fib1 = fib2
        fib2 = fib_next
        # check if the number is prime
        # if yes, increase the counter
        if is_prime(fib_next):
            p_fib_counter += 1
    return fib_next

