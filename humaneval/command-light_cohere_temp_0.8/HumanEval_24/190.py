```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number that divides n exactly
    Returns 0 if n is 0
    """
    if n < 0: return 0
    
    # Initialize the largest divisor found so far
    result = 1
    
    # Loop through potential divisors up to the square root of n
    for i in range(1, int(n**0.5)):
        if n % i == 0:
            result = max(result, i)
    
    return result
```