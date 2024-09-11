```python
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    This function works by dividing the input number n by the smallest prime number (2) as long as it's divisible.
    Then it increments the divisor by 1 and continues the process until the number n is reduced to 1.
    
    The last divisor that was used to divide n down to 1 is the largest prime factor of n.
    
    Parameters:
    n (int): The input number. Assume n > 1 and is not a prime.
    
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

This script defines a function `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. The function uses a while loop to divide `n` by the smallest prime number (2) as long as it's divisible, then increments the divisor by 1 and continues the process until `n` is reduced to 1. The last divisor that was used to divide `n` down to 1 is the largest prime factor of `n`. The script also includes test cases to demonstrate the function's correctness.