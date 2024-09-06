Here is a self-contained Python script with a function that solves the problem of finding the largest divisor of a given number:
```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer less than n that divides it evenly.
    """
    time complexity O(log(n))
    """
    return n // max(1, n // (n + 1))
```