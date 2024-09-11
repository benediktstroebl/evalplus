### Largest Prime Factor Function

```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    Args:
    n (int): An integer greater than 1.
    
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
print(largest_prime_factor(2048))  # Output: 2
```

### Explanation

This function works by dividing the input number `n` by the smallest prime number (`i`) as long as it's divisible. It starts from 2 and increments `i` by 1 in each iteration. If `n` is not divisible by `i`, it increments `i` by 1. When `n` is no longer divisible by `i`, `i` squared is greater than `n`, so the function returns `n`, which is the largest prime factor of the original number. 

This algorithm has a time complexity of O(sqrt(n)) because in the worst case, `i` will be at most sqrt(n), so the while loop will run at most sqrt(n) times.