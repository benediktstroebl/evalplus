### Largest Prime Factor Function
#### Python Implementation

```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    :param n: Input integer
    :return: Largest prime factor of n
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

# Example usage
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `largest_prime_factor` that takes an integer `n` and returns its largest prime factor. The function works by dividing `n` by the smallest prime number (2) as long as it's divisible, then moving on to the next number. This process continues until `n` is reduced to its largest prime factor.