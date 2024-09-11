```markdown
### Largest Prime Factor Function

#### Description
This script defines a function `largest_prime_factor` that returns the largest prime factor of a given number `n`.

#### Code

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

#### Explanation

This function uses a simple trial division method to find the largest prime factor of a given number `n`. It starts by checking divisibility from 2 and increments the divisor `i` until it finds a divisor that is not a factor of `n`. This divisor is then divided out of `n` to reduce it, and the process is repeated until `n` is reduced to its largest prime factor.