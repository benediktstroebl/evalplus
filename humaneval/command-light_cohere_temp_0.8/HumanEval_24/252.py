```python
def largest_divisor(n: int) -> int:
    """
    Return the largest number that divides n evenly and is smaller than n.
    """
   
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            return i
    return n
```