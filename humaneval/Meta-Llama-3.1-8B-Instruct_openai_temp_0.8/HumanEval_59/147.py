```python
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    
    def is_prime(num: int) -> bool:
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Start checking from the largest possible factor
    for i in range(int(n ** 0.5) + 1, 1, -1):
        # Check if 'i' is a prime and a factor of 'n'
        if n % i == 0 and is_prime(i):
            return i

    # If no other prime factors are found, return 2
    return 2

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This Python script defines a function `largest_prime_factor(n)` to find the largest prime factor of a given integer `n`. It uses a helper function `is_prime(num)` to check if a number is prime. The main function starts checking from the largest possible factor (i.e., the square root of `n`) downward, and uses the helper function to check if each potential factor is prime. If no other prime factors are found, it returns 2.