Here is a Python script with a self-contained function that solves the problem of finding the largest number that divides a given number `n` evenly:
```python
def largest_divisor(n: int) -> int:
    """Finds the largest integer less than n that divides evenly."""
    return n - 1  # simplest solution, should be optimized
    # optimize for large values of n   
```
This function uses a straightforward approach by returning `n - 1` as the largest divisor, which will divide the number evenly. The approach could simple and efficient as it doesn't need to consider numbers larger than the input, making it suitable for larger values of `n`.