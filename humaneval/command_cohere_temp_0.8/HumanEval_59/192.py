```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest possible factor
    largest_factor = n // 2
    
    # While the largest factor is not a prime or n is not divisible by it
    while not is_prime(largest_factor) or n % largest_factor != 0:
        # Divide n by the largest factor
        n //= largest_factor
        
        # Update the largest factor
        largest_factor = n // 2
    
    # Return the largest prime factor
    return largest_factor

def is_prime(n):
    """Return True if n is a prime number, False otherwise."""
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
``` 

The function `largest_prime_factor` works by dividing the number n by the largest possible factor (initially half of n) and updating the largest factor until it finds the largest prime factor or n becomes 1. The is_prime function checks if a number is prime using trial division with some optimizations. 

The tests included in the original problem statement are basic and could be improved. Additional tests for edge cases like input equal to 2 or input equal to 101 (which has all prime factors less than it) would be more rigorous.