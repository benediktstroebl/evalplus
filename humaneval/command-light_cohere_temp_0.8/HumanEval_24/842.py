```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number divisible by n, 
    which is also smaller than n
    """
    return n // max((n - 1) // i for i in range(2, int(n**0.5)))
```
This function efficiently calculates the largest divisor of n, ensuring that the result is always greater than or equal to the input number n, and smaller than n itself.