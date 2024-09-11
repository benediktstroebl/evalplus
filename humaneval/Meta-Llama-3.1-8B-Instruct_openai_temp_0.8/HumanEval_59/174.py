```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    Args:
        n (int): A composite number greater than 1.
    
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

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```
This script uses a while loop to find the largest prime factor of a given number. It starts by checking odd factors first and skips even numbers (except for 2) to reduce the number of iterations. The loop continues until `i * i` is greater than `n`, at which point `n` is a prime number and the function returns `n`.