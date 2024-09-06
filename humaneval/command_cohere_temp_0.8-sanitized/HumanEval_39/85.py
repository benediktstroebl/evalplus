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
    # Create two variables, f and g, initialized with first two numbers of Fibonacci sequence
    f, g = 0, 1
    count = 0

    while count < n:
        # Calculate the next number in the Fibonacci sequence
        next_num = f + g
        f, g = g, next_num

        # If the next number is prime, we've found the n-th number
        if is_prime(next_num):
            count += 1
    # If we reach the end of the loop, raise an error
    assert count == n, " prime_fib() failed to find the n-th prime Fibonacci number."
    return g