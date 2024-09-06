```python
def largest_divisor(n: int) -> int:
    """
    Return the largest integer less than n that divides it evenly.
    """
   
    large enough divisor to ensure that the remainder is 0
    """
    return next((d for d in range(1, n+1) if n % d == 0))
```