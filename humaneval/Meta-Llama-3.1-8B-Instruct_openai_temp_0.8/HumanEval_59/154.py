### Largest Prime Factor
#### Problem Description
Find the largest prime factor of a given number `n`.
#### Code Solution
```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
    n (int): The input number.

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
print(largest_prime_factor(2048))   # Output: 2
```
#### Explanation
This script uses a simple algorithm to find the largest prime factor of a given number `n`. The algorithm works by dividing `n` by the smallest prime number (`i`) as long as `n` is divisible by `i`. Once `n` is no longer divisible by `i`, increment `i` by 1. This process continues until `i` squared is greater than `n`, at which point `n` is the largest prime factor.

Note that we start `i` from 2 because it's the smallest prime number, and we use `i * i <= n` as the condition for the while loop because it's more efficient than checking every number up to `n`.