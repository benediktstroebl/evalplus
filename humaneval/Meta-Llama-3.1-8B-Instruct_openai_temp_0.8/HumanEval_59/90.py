### Largest Prime Factor
#### Problem Description
This script solves the problem of finding the largest prime factor of a given number.
#### Solution

```python
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

# Example usage:
if __name__ == "__main__":
    print(largest_prime_factor(13195))  # Output: 29
    print(largest_prime_factor(2048))   # Output: 2
```

This script works by dividing the input number `n` by the smallest prime number `i` (which starts at 2) as long as `n` is divisible by `i`. If `n` is not divisible by `i`, we increment `i` by 1. This process continues until `i` is greater than the square root of `n`. At this point, `n` is guaranteed to be a prime number, so we return it as the largest prime factor.