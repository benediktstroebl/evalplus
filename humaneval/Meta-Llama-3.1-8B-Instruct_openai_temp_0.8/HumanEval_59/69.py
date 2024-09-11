```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n.
    
    Assume n > 1 and is not a prime.
    
    :param n: The number for which to find the largest prime factor
    :return: The largest prime factor of n
    """
    def is_prime(num: int) -> bool:
        """
        Check if a number is prime.
        
        :param num: The number to check
        :return: True if num is prime, False otherwise
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    largest_factor = 1
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0 and is_prime(i):
            largest_factor = i
            n = n // i
    if is_prime(n) and n > largest_factor:
        largest_factor = n
    return largest_factor

# Test cases
import doctest
doctest.testmod()

print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script first defines a helper function `is_prime` to check if a number is prime. Then, it iterates over all numbers from 2 to the square root of `n`. If `n` is divisible by `i` and `i` is prime, it updates the largest factor and divides `n` by `i`. After the loop, if `n` itself is prime and greater than the current largest factor, it updates the largest factor to `n`. Finally, it returns the largest factor.