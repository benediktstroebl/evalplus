```python
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.

    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def is_prime(num: int) -> bool:
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Start checking from 2
    i = 2
    while i * i <= n:
        if n % i:
            # If i does not divide n, increment i
            i += 1
        else:
            # If i divides n, check if i is prime
            if is_prime(i):
                # If i is prime, it's a prime factor of n
                n //= i
            else:
                # If i is not prime, increment i
                i += 1

    # At the end, n will be the largest prime factor
    return n

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. It uses a helper function `is_prime` to check if a number is prime. The main function iterates from 2 to the square root of `n`, checking for divisibility and primality. If `n` is not divisible by a prime number `i`, it increments `i`. If `n` is divisible by a prime `i`, it checks if `i` is prime and divides `n` by `i` if it is. At the end, `n` will be the largest prime factor of the original input.