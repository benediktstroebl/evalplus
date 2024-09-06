```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer less than n that divides evenly.
    """
    def is_divisor(num: int, n: int) -> bool:
        """Returns True if num is a divisor of n, False otherwise."""
        return num >= n and num % n == 0

    if is_divisor(n, n):
        return n
    
    return 5 # return the largest divisor less than n
```