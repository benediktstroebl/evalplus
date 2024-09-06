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
    Returns the n-th number that is a Fibonacci number and it's also prime.
    """
    # Create two variables, f and g, initialized to the first two numbers of the Fibonacci sequence
    f, g = 0, 1
    count = 0

    while count < n:
        # Calculate the next Fibonacci number
        f, g = g, f + g
        count += 1

        # Check if the calculated number is prime
        if is_prime(f):
            return f
    # If no prime Fibonacci number is found after n attempts, return the original n
    return n