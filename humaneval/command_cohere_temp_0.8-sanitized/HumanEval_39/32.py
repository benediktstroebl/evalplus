def is_prime(n):
    """
    Checks if a number is prime
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_fib(n):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    # Create two variables, f and g, initialized with the first two numbers of Fibonacci sequence
    f, g = 0, 1
    count = 0

    while count < n:
        # If f is prime, return it
        if is_prime(f):
            return f
        # To avoid repeated numbers in the Fibonacci sequence, we increment g by f and set f equal to g
        g, f = f, g + f
        count += 1
    # If we finish the loop without finding a prime Fibonacci number, return -1
    return -1