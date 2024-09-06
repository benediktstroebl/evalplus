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
    # Initialize two variables for the first two fibonacci numbers
    x, y = 0, 1
    count = 0

    while count < n:
        # Calculate the next Fibonacci number
        x, y = y, x + y
        count += 1

        # Check if the calculated number is prime
        if is_prime(x):
            if count == n:
                return x
            continue
        if count == n:
            return x

    # This clause should never be reached if the inputs are correct
    return x