```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n. 
    Assume n > 1 and is not a prime.

    Parameters:
    n (int): The input number.

    Returns:
    int: The largest prime factor of n.
    """
    def is_prime(num: int) -> bool:
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Start checking from the largest possible factor
    for i in range(int(n**0.5) + 1, 1, -1):
        # Check if i is a factor of n and is prime
        if n % i == 0 and is_prime(i):
            return i

    # If no prime factors larger than sqrt(n) are found, the number itself is the largest prime factor
    return n


# Example usage
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. The function uses a helper function `is_prime` to check if a number is prime. The main function then iterates from the largest possible factor down to 1, checking if each factor is prime using the `is_prime` function. If it finds a prime factor, it returns it. If no prime factors are found, it returns the number itself, since it's the largest prime factor in that case.