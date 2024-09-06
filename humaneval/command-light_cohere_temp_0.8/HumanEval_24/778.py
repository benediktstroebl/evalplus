```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number that divides n exactly without a remainder.
    """
    Note that this solution is not optimized for performance, and may not be the most efficient method.
    """
   
    approach:
    return n if n % 2 == 0
    else n+1
```