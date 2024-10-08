def is_prime(n):
    """Helper function to check if the given number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """Function to check if the given number is the multiplication of 3 prime numbers."""
    count = 0
    for i in range(2, a+1):
        if is_prime(i) and a % i == 0:
            count += 1
            if count > 3:
                return False
    return count == 3
