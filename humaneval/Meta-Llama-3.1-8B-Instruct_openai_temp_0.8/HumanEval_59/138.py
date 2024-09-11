```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
    n (int): A number greater than 1 that is not a prime.

    Returns:
    int: The largest prime factor of n.
    """
    def is_prime(num: int) -> bool:
        """
        Check if a number is prime.

        Args:
        num (int): The number to check.

        Returns:
        bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Start from the largest possible factor, which is n // 2
    for i in range(n // 2, 1, -1):
        # Check if the factor is prime
        if n % i == 0 and is_prime(i):
            # If the factor is prime, return it
            return i
    # If no prime factor is found, return 2 (the smallest prime number)
    return 2

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
print(largest_prime_factor(600851475143)) # Output: 6857
```

This solution defines a helper function `is_prime(num)` to check if a number is prime. Then, it starts from the largest possible factor `n // 2` and checks each factor to see if it's prime. If it finds a prime factor, it returns that factor. If no prime factor is found, it returns 2 (the smallest prime number).