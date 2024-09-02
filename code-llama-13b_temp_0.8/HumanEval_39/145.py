

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
    # Index of the current number in the Fibonacci sequence
    current_fib_index = 2
    # Index of the current prime number
    current_prime_index = 1
    # Keep getting the next Fibonacci number until we get the n-th one
    while current_fib_index < n:
        # Get the next Fibonacci number
        next_fib = fib_number(current_fib_index)
        # Check if it is prime
        if prime_check(current_prime_index, next_fib):
            # Increase the number of found prime Fibonacci numbers by one
            current_fib_index += 1
            # Return the Fibonacci number if this is the last one
            if current_fib_index == n:
                return next_fib
        # If it is not prime, skip it
        else:
            current_prime_index += 1
    return -1

