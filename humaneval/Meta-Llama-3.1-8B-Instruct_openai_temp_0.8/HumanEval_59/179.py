### Largest Prime Factor Function
Here's the self-contained Python script that implements the `largest_prime_factor` function:
```markdown
### Code
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
print(largest_prime_factor(13195))  # 29
print(largest_prime_factor(2048))   # 2
```

### Explanation
The function `largest_prime_factor` uses a simple trial division method to find the largest prime factor of the input number `n`. It starts with the smallest prime number `i = 2` and keeps dividing `n` by `i` as long as `n` is divisible by `i`. Once `n` is no longer divisible by `i`, we increment `i` by 1 and repeat the process until `i` is greater than the square root of `n`. At this point, `n` itself is the largest prime factor of the original number.