### Largest Prime Factor Function
```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.
    Assume n > 1 and is not a prime.

    Args:
        n (int): A positive integer greater than 1.

    Returns:
        int: The largest prime factor of n.

    Example:
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
print(largest_prime_factor(2048))  # Output: 2
```
This script defines a function `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. It uses a while loop to continuously divide `n` by the smallest divisor (starting from 2) until it finds a divisor that is not a factor of `n`. The loop continues until `i` is greater than the square root of `n`, at which point `n` is guaranteed to be a prime number. The function then returns `n`, which is the largest prime factor of the original number.