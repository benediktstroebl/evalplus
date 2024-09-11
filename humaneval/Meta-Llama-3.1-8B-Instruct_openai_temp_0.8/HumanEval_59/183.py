```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    Args:
        n (int): A positive integer greater than 1.
    
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

This script uses a simple algorithm to find the largest prime factor of a given number. It starts by checking divisibility from 2 and increments the divisor until it finds a number that divides the input `n`. Once a divisor is found, it divides `n` by the divisor and continues the process with the new value of `n`. This continues until `n` is reduced to its largest prime factor. The function returns this largest prime factor.