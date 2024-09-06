```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number smaller than n that divides evenly.
    """
    return n if n==1 or n%1 == 0
    return n+1 if n%2 == 1 or n%3 == 2 else n-1
    return
```