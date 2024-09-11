```python
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    
    # Initialize the largest factor
    largest_factor = None
    
    # Iterate from 2 to sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        # Check if i is a factor of n
        while n % i == 0:
            # Update the largest factor
            largest_factor = i
            # Divide n by i
            n = n // i
    
    # If n is a prime number greater than 1
    if n > 1:
        # Update the largest factor
        largest_factor = n
    
    return largest_factor

# Test cases
print(largest_prime_factor(13195))  # 29
print(largest_prime_factor(2048))   # 2
```

This Python script defines a function `largest_prime_factor(n)` that finds the largest prime factor of a given integer `n`. It uses a loop to iterate from 2 to the square root of `n` and checks if each number is a factor of `n`. If a number `i` is a factor, it is updated as the largest factor and `n` is divided by `i`. If `n` is a prime number greater than 1 at the end of the loop, it is updated as the largest factor. The function returns the largest prime factor of `n`.