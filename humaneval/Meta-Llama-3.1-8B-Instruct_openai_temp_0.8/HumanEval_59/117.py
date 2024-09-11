```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.
    
    Assume n > 1 and is not a prime.
    
    :param n: The number to find the largest prime factor of
    :return: The largest prime factor of n
    """
    
    def is_prime(num: int) -> bool:
        """
        Helper function to check if a number is prime.
        
        :param num: The number to check for primality
        :return: True if num is prime, False otherwise
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Start checking from the largest possible factor (n / 2) down to 2
    for i in range(n // 2, 1, -1):
        # If i is a factor of n and is prime, it's the largest prime factor
        if n % i == 0 and is_prime(i):
            return i
    # If no prime factors were found, n itself is a prime number
    return n

# Test cases
print(largest_prime_factor(13195))  # Should print 29
print(largest_prime_factor(2048))   # Should print 2
```

This script defines a function `largest_prime_factor` that finds the largest prime factor of a given number `n`. It uses a helper function `is_prime` to check if a number is prime. The `largest_prime_factor` function iterates over all numbers from `n/2` down to 2, checking if each number is a factor of `n` and is prime. If it finds a prime factor, it returns that number. If no prime factors are found, the function returns `n`, indicating that `n` itself is a prime number.