```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number that divides n evenly, smaller than n
    """
    return next((i for i in range(1, int(n ** 0.25) if n % i == 0))
```