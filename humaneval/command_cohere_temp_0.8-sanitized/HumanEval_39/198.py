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
    if n <= 0:
        raise ValueError("n must be positive")
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # The n-th Fibonacci prime would be the larger of the two numbers
        # in the (n-1)th Fibonacci pair
        prev, curr = 5, 8
        for _ in range(3, n):
            # Save the previous Fibonacci number
            prev = curr
            # Calculate the next Fibonacci number
            curr = prev + curr
            if is_prime(curr):
                return curr