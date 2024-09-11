### Largest Prime Factor Function
```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.

    Args:
    n (int): The number to find the largest prime factor of. Assume n > 1 and is not a prime.

    Returns:
    int: The largest prime factor of n.

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

# Example use cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))  # Output: 2
```
In this script, we start by checking divisibility from the smallest prime number (2). If `n` is divisible by `i`, we divide `n` by `i` and continue the loop. If `n` is not divisible by `i`, we increment `i` by 1 and continue the loop. This process continues until `i` is greater than the square root of `n`. At this point, `n` will be the largest prime factor of the original number.