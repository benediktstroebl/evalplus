### Largest Prime Factor
#### Problem Statement
Find the largest prime factor of a given integer `n`.

#### Solution
```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n.
    
    Args:
    n: An integer (assumed to be greater than 1 and not a prime).
    
    Returns:
    The largest prime factor of n.
    
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

# Example usage
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```
#### Explanation
This script uses a simple trial division method to find the largest prime factor of `n`. It iteratively divides `n` by the smallest prime factor (initially `2`) as long as `n` is divisible by it. Once `n` is no longer divisible, the next prime factor is found by incrementing `i`. The process continues until `n` is reduced to its largest prime factor.

The time complexity of this algorithm is approximately O(sqrt(n)), making it efficient for large inputs.