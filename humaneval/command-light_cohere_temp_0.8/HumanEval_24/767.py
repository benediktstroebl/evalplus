```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number that divides n evenly, 
    smaller than n
    """
    return next((d for d in range(1, n+1) if not n % d), n)
```