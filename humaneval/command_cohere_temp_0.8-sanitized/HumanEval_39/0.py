def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_fib(n):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    # Create two variables, f and g, initialized to the first two numbers of the Fibonacci sequence
    f = 0
    g = 1
    count = 0

    while count < n:
        # If f is prime, return it
        if is_prime(f):
            return f
        # Generate the next Fibonacci number
        count += 1
        x = f + g
        f = g
        g = x

    # If we reach this line, the desired index n is out of bounds
    return None