```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number that divides n exactly
    """
    return [i for i in range(1, n+1) if n % i == 0]
```