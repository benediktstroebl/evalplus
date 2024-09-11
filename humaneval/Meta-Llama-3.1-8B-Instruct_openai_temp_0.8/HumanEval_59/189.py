### Largest Prime Factor of a Number
#### Problem Description
This script calculates the largest prime factor of a given number.

#### Code
```python
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.

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
            # If n is not divisible by i, increment i
            i += 1
        else:
            # If n is divisible by i, update n and continue
            n //= i
    return n

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

#### Explanation
This script iterates through all numbers from 2 to the square root of `n` to find its largest prime factor. If `n` is divisible by `i`, it updates `n` to be `n / i`. The loop continues until `n` is no longer divisible by any number up to its square root, at which point `n` itself is the largest prime factor.

This solution has a time complexity of O(sqrt(n)) because it only needs to check up to the square root of `n` to find its largest prime factor.