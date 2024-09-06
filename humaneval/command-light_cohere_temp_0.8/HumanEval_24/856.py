```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number that divides n evenly, smaller than n.
    """
    = n
    if n <= 1:
        return n
    else:
        return max((i for i in range(1, n+1) if n % i == 0)) + 1
```