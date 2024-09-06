```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer divisor of n that is less than n
    """
    # Handling negative numbers by converting to non-negative
    n = n >= 0 ? n : -n
    
    # Largest divisor less than n
    i = 2
    
    while i * i <= n:
        if n % i == 0:
            return i
        i += 1
    
    # If no such divisors exist, return n itself
    return n
```