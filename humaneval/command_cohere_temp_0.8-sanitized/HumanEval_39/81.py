def is_prime(n):
    """
    Checks if a number is prime
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_fib(n):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    # Create two variables, f and g, initialized to the first two numbers of the Fibonacci sequence
    f, g = 0, 1
    count = 0

    while count < n:
        # If f is prime, return it
        if is_prime(f):
            return f
        # If g is prime, return it
        if is_prime(g):
            return g
        # Create the next Fibonacci number
        count += 1
        f, g = g, f + g

    # If we reach the end of the loop, the requested number is larger than the max Fibonacci number
    return None