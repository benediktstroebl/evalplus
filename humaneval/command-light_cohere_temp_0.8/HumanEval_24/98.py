Here's the self-contained Python function that finds the largest divisor of a given number:
```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer which divides the given number evenly,
    ensuring the result is less than the given number.
    """
    def loop_ divisor(num: int) -> int:
        while any(num % div for div in range(1, int(n ** .5))):
            divisor = n // div
            if divisor == num:
                return divisor
            n -= divisor
    return n
```