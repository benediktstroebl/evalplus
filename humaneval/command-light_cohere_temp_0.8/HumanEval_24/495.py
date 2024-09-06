```python
def largest_divisor(n: int) -> int:
    """
    Finds the largest number that divides n evenly, smaller than n.
    """
    return n if n % 1 == 0
    return n+1 if n % 2 == 0 
    else:
        return 1 + largest_divisor(n//2)
```