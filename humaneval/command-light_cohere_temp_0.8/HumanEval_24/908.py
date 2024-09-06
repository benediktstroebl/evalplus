```python
def largest_divisor(n: int) -> int:
    """
    Finds the largest divisor of n that is less than n.
    Returns -1 if n is 1, otherwise returns the largest integer less than n that divides evenly into n.
    """

    for divisor in range(2, n):
        if n % divisor == 0:
            return divisor
    return -1
```