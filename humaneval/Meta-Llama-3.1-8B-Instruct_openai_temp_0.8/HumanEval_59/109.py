### Problem Solution
```python
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.

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

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```
### Explanation

This function `largest_prime_factor` calculates the largest prime factor of a given number `n`. It uses a simple trial division method to find the prime factors.

Here's how it works:

1. We start with `i` as 2 (the smallest prime number).
2. We check if `i` is a factor of `n` by using the modulo operator (`n % i`). If it's not, we increment `i` by 1.
3. If `i` is a factor of `n`, we divide `n` by `i` to remove this factor.
4. We repeat steps 2-3 until `i` is greater than the square root of `n`. This is because a larger factor of `n` must be a multiple of a smaller factor that has already been checked.
5. At the end of the loop, `n` is the largest prime factor of the original input.

The time complexity of this algorithm is approximately O(sqrt(n)), making it efficient for large input numbers.