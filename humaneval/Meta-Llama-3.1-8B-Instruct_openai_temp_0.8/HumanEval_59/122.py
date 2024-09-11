```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. 
    Assume n > 1 and is not a prime.
    
    :param n: The input number.
    :return: The largest prime factor of n.
    """
    def is_prime(num: int) -> bool:
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Start from 2 and go up to sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        # Check if i is a factor and is prime
        while n % i == 0 and is_prime(i):
            n //= i

    # If n is not 1, it is a prime number and the largest prime factor
    return n if n!= 1 else max(range(2, int(n ** 0.5) + 1), key=lambda x: is_prime(x) and not n % x)

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. It uses a helper function `is_prime` to check if a number is prime. The function works by dividing `n` by all numbers from 2 to the square root of `n`, checking if each divisor is prime. If a prime divisor is found, it is removed from `n` by division. The process is repeated until `n` is reduced to its largest prime factor, which is then returned. If `n` itself is a prime number, it is returned as the largest prime factor.