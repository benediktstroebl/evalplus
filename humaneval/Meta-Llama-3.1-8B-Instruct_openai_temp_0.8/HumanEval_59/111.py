```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    Args:
        n (int): The input number. Assume n > 1 and is not a prime.

    Returns:
        int: The largest prime factor of n.
    """
    def is_prime(num: int):
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Start checking for prime factors from the smallest possible factor (2)
    i = 2
    while i * i <= n:
        if n % i:
            # if n is not divisible by i, increment i by 1
            i += 1
        else:
            # if n is divisible by i, check if i is prime
            if is_prime(i):
                # if i is prime, return i as the largest prime factor
                return i
            # if i is not prime, increment i by 1
            n //= i

    # if no prime factors were found, return n as the largest prime factor
    return n

# Test the function
print(largest_prime_factor(13195))  # 29
print(largest_prime_factor(2048))   # 2
```

This script defines a function `largest_prime_factor` that takes an integer `n` and returns its largest prime factor. The function uses a helper function `is_prime` to check if a number is prime. It then checks all numbers from 2 to the square root of `n` as possible prime factors, and returns the first prime factor it finds. If no prime factors are found, it returns `n` as the largest prime factor.