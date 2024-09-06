```python
def largest_divisor(n: int) -> int:
    """
    Finds the largest number which divides the given number evenly, 
    smaller than it
    """
    return max(range(n+1), key=lambda x: x % n == 0)
```