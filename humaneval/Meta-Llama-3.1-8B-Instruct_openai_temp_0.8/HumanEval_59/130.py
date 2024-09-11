```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
        n (int): A positive integer greater than 1.

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
print(largest_prime_factor(600851475143))  # Output: 6857
```

This script uses the trial division method to find the largest prime factor of a given number. The algorithm works by dividing the input number `n` by increasing integers `i` until it finds a divisor. If `n` is divisible by `i`, it divides `n` by `i` and continues with the next integer. If `n` is not divisible by `i`, it increments `i` by 1 and continues with the next integer. This process continues until `i` is greater than the square root of `n`, at which point `n` is guaranteed to be a prime number. The function then returns `n` as the largest prime factor.