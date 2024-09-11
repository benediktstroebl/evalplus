```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
        n (int): The number to find the largest prime factor of.

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

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. It uses a simple trial division method to find the largest prime factor.

Here's how it works:

1.  We start by checking if `n` is divisible by `i`, where `i` is the smallest prime number (`2`).
2.  If `n` is not divisible by `i`, we increment `i` by `1`.
3.  If `n` is divisible by `i`, we divide `n` by `i` and repeat the process.
4.  We continue this process until `i` is greater than the square root of `n`. This is because a larger factor of `n` would have a corresponding smaller factor that has already been checked.
5.  At this point, `n` is a prime number and is the largest prime factor of the original number. We return `n`.

The time complexity of this script is O(√n), which is efficient for large inputs.