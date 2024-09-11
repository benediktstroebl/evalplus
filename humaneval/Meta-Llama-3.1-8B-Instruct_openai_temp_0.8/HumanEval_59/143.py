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

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```
This script uses a simple trial division method to find the largest prime factor of a given number `n`. It iterates from 2 to the square root of `n` (inclusive), checking if `n` is divisible by the current number `i`. If `n` is divisible, it divides `n` by `i`. If `n` is not divisible, it increments `i`. This process continues until `i` is greater than the square root of `n`, at which point `n` is returned as the largest prime factor.