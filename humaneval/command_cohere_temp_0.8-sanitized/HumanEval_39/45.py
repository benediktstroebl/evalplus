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
        # Stores the next Fibonacci number
        x, y = y, x + y
        count += 1

    # Convert count to int since it's implicitly cast to int in return statement
    return next((f for f in [x, y] if is_prime(f)), None)