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
    # Initialize two variables for the first two numbers of the Fibonacci sequence.
    x, y = 0, 1
    count = 0

    while count < n:
        # Calculate the next Fibonacci number.
        next_num = x + y
        count += 1

        # Check if the next Fibonacci number is prime.
        if is_prime(next_num):
            if count == n:
                return next_num
        x, y = y, next_num

    # If no prime Fibonacci number is found within the given range, return None.
    return None