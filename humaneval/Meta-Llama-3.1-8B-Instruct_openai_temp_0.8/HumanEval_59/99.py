### Largest Prime Factor Function
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
This script implements the `largest_prime_factor` function, which takes an integer `n` as input and returns its largest prime factor. The function uses a simple trial division approach to find the largest prime factor. It iteratively divides the number `n` by the smallest prime number (2) as long as it is divisible, then increments the divisor until it finds a number that is not divisible. This process continues until the input number is reduced to its largest prime factor.