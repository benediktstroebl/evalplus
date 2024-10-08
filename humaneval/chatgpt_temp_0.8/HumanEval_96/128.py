def is_prime(num):
    """Helper function to check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_up_to(n):
    """Function to return an array of prime numbers up to n."""
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes
