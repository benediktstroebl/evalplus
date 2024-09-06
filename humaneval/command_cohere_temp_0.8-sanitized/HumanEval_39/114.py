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
    # Initialize two variables for the first two fibonacci numbers
    x, y = 0, 1
    count = 0

    while count < n:
        # Increment the count of prime fibonacci numbers found
        count += 1

        # If the current fibonacci number is prime, return it
        if is_prime(x):
            return x

        # Prepare for the next Fibonacci number
        x, y = y, x + y

    # If we reach the end of the loop, return the last prime Fibonacci number encountered
    return x