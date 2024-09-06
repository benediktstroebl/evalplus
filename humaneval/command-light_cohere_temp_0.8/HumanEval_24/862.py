```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number which divides n exactly
    """
    return max((i) for i in range(1,int(n**0.25))
```  This is a self-contained function that takes an integer n and returns the largest integer that divides n exactly without a remainder.