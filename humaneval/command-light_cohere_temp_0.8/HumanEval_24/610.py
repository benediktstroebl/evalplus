```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer divisor of n that is less than n.
    """
    for i in range(1,int(n**0.5)):
        if n % i == 0:
            return i
    else:
        return None
```