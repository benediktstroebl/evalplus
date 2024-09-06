```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number that divides n evenly, 
    smaller than n.
    """
    for x in range(1, n):
        if n % x == 0:
            return x
    return n
```