```python
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script uses a simple algorithm to find the largest prime factor of a given number `n`. It starts from 2 and checks each number up to the square root of `n` to see if it divides `n`. If it does, `n` is divided by that number. This process continues until `n` is no longer divisible by any of the numbers up to its square root. At that point, `n` is the largest prime factor of the original number. 

This algorithm works efficiently because a larger factor of `n` must be a multiple of a smaller factor that has already been checked. Therefore, we only need to check up to the square root of `n`.