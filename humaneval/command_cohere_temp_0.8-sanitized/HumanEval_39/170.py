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
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    # Make sure n is positive
    n = abs(n)
    # Initialize variables for the first two Fibonacci numbers
    a, b = 0, 1
    count = 0

    while True:
        # Check if the next Fibonacci number is prime
        if is_prime(a):
            count += 1
            if count == n:
                return a
            a, b = b, a + b

        # Make sure the loop doesn't run forever
        if a > 100:
            break

    return None