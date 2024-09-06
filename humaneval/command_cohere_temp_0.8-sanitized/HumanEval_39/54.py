def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def prime_fib(n):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    # Make sure n is positive
    n = abs(n)
    if n == 1:
        return 2
    elif n == 2:
        return 3
    elif n == 3:
        return 5
    else:
        # The n-th Fibonacci number is the (sum of the (n-1th and n-2th number))
        # We just need to find the n-2nd and n-1th numbers and sum them
        # While the n-1st number is prime, the n-2nd needs to be prime as well
        # because their sum must be prime as well
        prev, curr = 0, 1
        count = 0
        while not is_prime(curr):
            prev, curr = curr, prev + curr
            count += 1
        # If the countdown reaches infinity, it means the n-th Fibonacci number
        # is too large and exceeds the realm of prime numbers
        if count >= 10000:
            return None
        return prev