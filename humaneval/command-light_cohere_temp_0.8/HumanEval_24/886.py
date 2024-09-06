```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number that divides n exactly without a remainder, 
    ensuring it's smaller than n.

    Example:
        1.
    """
   
    1 + 2 + 3 = 4
    """
    return max((i for i in range(1, n+1) if n % i == 0))
```