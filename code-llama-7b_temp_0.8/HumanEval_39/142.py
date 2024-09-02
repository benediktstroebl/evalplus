

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

    # Initialize two variables to hold the two Fibonacci numbers
    fib1 = 1
    fib2 = 2

    # Initialize the third variable to hold the current Fibonacci number.
    # This will be used to store the n-th number that is both a Fibonacci
    # number and a prime.
    fib3 = 3

    # Start the loop
    # The loop ends when we have found the Fibonacci number that is
    # both prime and the n-th Fibonacci number.
    i = 2

    while i < n:
        # Swap the variables so that the next Fibonacci number is stored in
        # fib1, and the next-to-next Fibonacci number is stored in fib2
        fib1, fib2 = fib2, fib1+fib2
        # Test if the fib3 variable is prime
        if is_prime(fib3):
            # If it is prime, then check if this is the n-th prime.
            i += 1

    # fib3 has the n-th prime that is also a Fibonacci number
    return fib3

