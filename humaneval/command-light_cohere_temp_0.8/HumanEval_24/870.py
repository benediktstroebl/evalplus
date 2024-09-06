```python
def largest_divisor(n: int) -> int:
    """
    Return the largest number that divides n evenly, 
    smaller than n. 
    Example:
        for x from 1 to n do 
            if n % x == 0:
                return x
    """
    return max([x for x in range(1, n+1) if n % x == 0])
```