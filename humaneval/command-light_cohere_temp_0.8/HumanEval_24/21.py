```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer less than n, 
    that divides n evenly.
    """
    Recursive function that returns the greatest integer that 
    does not exceed n and divides it evenly 
    without remainder.
    """
    Try: 0
    while n % 2 == 0:
        n //= 2
    return n
```