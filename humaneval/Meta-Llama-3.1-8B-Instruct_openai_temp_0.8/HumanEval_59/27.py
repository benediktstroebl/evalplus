### Largest Prime Factor
#### Problem Description
Given an integer `n` greater than 1 and not a prime, find its largest prime factor.

#### Solution
```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.
    
    Args:
    n (int): An integer greater than 1 and not a prime.
    
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

# Example usage:
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

#### Explanation
This function uses a simple trial division approach. It starts from 2 and checks if `n` is divisible by the current number `i`. If `n` is divisible, it divides `n` by `i` and continues with the new value of `n`. If `n` is not divisible by `i`, it increments `i` by 1. This process continues until `i` is greater than the square root of `n`. At this point, `n` is guaranteed to be a prime number, and it is the largest prime factor of the original `n`.