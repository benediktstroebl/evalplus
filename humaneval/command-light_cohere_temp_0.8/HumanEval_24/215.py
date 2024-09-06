```python
def largest_divisor(n: int) -> int:
    """
    Return the largest number less than n, 
    that divides n exactly
    """
    return next((i for i in range(1, n+1) if n % i == 0))
```