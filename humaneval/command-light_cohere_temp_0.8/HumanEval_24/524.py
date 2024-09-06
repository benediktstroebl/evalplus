```python
def largest_divisor(n: int) -> int:
    """Finds the largest integer divisor of n that is less than n"""
    if n <= 1:
        return 1
    
    # Ensure n is odd before finding the largest divisor
    n += 1
    
    while n % 2 == 0:
        n += 1
    
    return n
```