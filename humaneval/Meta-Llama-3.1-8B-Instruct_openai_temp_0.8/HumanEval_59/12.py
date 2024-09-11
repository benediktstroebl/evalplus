```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. 
    Assume n > 1 and is not a prime.

    Args:
    n (int): A composite number.

    Returns:
    int: The largest prime factor of n.

    Examples:
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

This script uses the Sieve of Eratosthenes or trial division method to find the largest prime factor of a given number. 

1. Start with the smallest prime number, 2.
2. If the number `n` is divisible by `i`, then `i` is a factor and we divide `n` by `i`. We repeat this step until `n` is no longer divisible by `i`.
3. We increment `i` by 1 and repeat steps 2 and 3 until `i * i` is less than or equal to `n`.
4. At this point, `n` is the largest prime factor of the original number.