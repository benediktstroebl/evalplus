### Largest Prime Factor Function
#### Problem: Find the largest prime factor of a given number `n`
#### Python Solution

```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.
    Assume n > 1 and is not a prime.

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
print(largest_prime_factor(13195))  # Expected output: 29
print(largest_prime_factor(2048))   # Expected output: 2
```

This script uses a simple algorithm to find the largest prime factor of a given number. It starts by dividing the number `n` by the smallest prime number `i`, which is 2. If `n` is divisible by `i`, it divides `n` by `i` and repeats the process with the new value of `n`. If `n` is not divisible by `i`, it increments `i` by 1 and repeats the process. This continues until `i` is greater than the square root of `n`. At this point, `n` is the largest prime factor of the original number.