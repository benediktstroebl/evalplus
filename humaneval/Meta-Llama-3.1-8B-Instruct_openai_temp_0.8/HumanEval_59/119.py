### Largest Prime Factor of a Number
#### Problem Description

Write a function `largest_prime_factor(n: int)` that takes an integer `n` as input, 
where `n > 1` and is not a prime. The function should return the largest prime factor of `n`.

#### Solution
```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
        n (int): The input number.

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

# Example usage:
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

### Explanation

This function uses a simple trial division method to find the largest prime factor of `n`. 
Here's a step-by-step breakdown:

1. Start with `i = 2`, the smallest prime number.
2. Check if `i * i <= n`. If not, `i` is already larger than the square root of `n`, 
   so we can break the loop.
3. If `n` is divisible by `i`, then `i` is a prime factor of `n`. Divide `n` by `i` to remove this factor.
4. Increment `i` by 1 and repeat steps 2-3 until `n` is no longer divisible by `i`.
5. At this point, `n` is a prime number and must be the largest prime factor of the original `n`. Return `n`.