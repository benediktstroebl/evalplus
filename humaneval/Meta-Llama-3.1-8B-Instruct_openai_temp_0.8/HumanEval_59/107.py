### Largest Prime Factor
#### Problem Description
Write a Python function to find the largest prime factor of a given number.

#### Code
```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Parameters:
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

#### Explanation
This script defines a function `largest_prime_factor(n)` that finds the largest prime factor of a given number `n`. It uses a while loop to divide `n` by the smallest divisor, which is 2, as long as it is divisible. If `n` is not divisible by 2, it increments the divisor by 1. This process continues until `n` is no longer divisible by the divisor. At this point, `n` will be the largest prime factor of the original number.