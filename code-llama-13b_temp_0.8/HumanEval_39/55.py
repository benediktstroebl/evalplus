

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

    # Initialize the Fibonacci sequence.
    a, b = 0, 1
    i = 0

    # Loop through the Fibonacci sequence until we
    # find the number that is a Fibonacci prime.
    while True:

        # If the current number is prime.
        if is_prime(b):

            # Increase the counter.
            i += 1

            # If the counter is equal to the
            # number of n, then return the number.
            if i == n:
                return b

        # Compute the next Fibonacci number.
        a, b = b, a + b

