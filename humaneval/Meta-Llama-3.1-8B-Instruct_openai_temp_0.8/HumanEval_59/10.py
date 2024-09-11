### Largest Prime Factor Function
```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. 
    Assume n > 1 and is not a prime.

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

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```
This Python function uses a loop to divide the input number `n` by the smallest prime factor until it is no longer divisible. It keeps track of the largest prime factor seen so far. This process continues until `n` is reduced to its largest prime factor. The function returns this largest prime factor.