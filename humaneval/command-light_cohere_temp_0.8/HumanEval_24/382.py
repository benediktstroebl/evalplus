```python
def largest_divisor(n: int) -> int:
    """
    Finds the largest integer divisor of n that is less than n.
    """
    for i in range(1,int(n**0.5)):
        if n % i == 0:
            return i
    return -1
```