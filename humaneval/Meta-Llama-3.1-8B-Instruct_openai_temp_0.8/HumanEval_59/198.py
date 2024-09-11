```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.
    
    Assume n > 1 and is not a prime.

    :param n: Input number
    :return: Largest prime factor of n
    """
    def is_prime(num: int) -> bool:
        """
        Check if a number is prime.
        
        :param num: Number to check
        :return: True if num is prime, False otherwise
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    largest_factor = 1
    for i in range(2, n + 1):
        # Check if i is a factor of n and is prime
        if n % i == 0 and is_prime(i):
            largest_factor = max(largest_factor, i)
    return largest_factor

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script uses a helper function `is_prime` to check if a given number is prime. It then iterates through all numbers from 2 to `n`, checks if each number is a factor of `n` and is prime, and updates `largest_factor` accordingly. The function returns the largest prime factor of `n`.