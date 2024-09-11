### Largest Prime Factor
#### A Python Function to Find the Largest Prime Factor of a Given Number

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

This script defines a function `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. The function uses a while loop to try dividing the input number `n` by increasing integers `i`, starting from 2. When `n` is divisible by `i`, it is divided by `i` and the process is repeated with the new value of `n`. The loop continues until `n` is no longer divisible by `i`, at which point `n` itself is the largest prime factor.