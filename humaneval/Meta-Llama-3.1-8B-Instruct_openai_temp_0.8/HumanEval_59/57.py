### Largest Prime Factor

This script calculates the largest prime factor of a given number `n`.

```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
    n (int): The input number.

    Returns:
    int: The largest prime factor of n.
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

# Example usage:
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

In this script, we use a simple trial division method to find the largest prime factor of `n`. We start by dividing `n` by the smallest prime number, which is 2, and continue dividing it by increasing integers until we reach the square root of `n`. If `n` is not divisible by the current number `i`, we increment `i` by 1. If `n` is divisible by `i`, we divide `n` by `i` and repeat the process. This process continues until `n` is reduced to its largest prime factor.