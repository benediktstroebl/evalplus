```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer divisor of n that is less than n
    """
    return n // max(1, n - 1)
```  This Python code defines a function called `largest_divisor` that takes an integer n as input and returns the largest integer divisor of n. This divisor is smaller than n, ensuring that the function returns a positive integer value. The `max` function is used to compare with the minimum value, and `n // ` is used to return the largest integer divisor of n.