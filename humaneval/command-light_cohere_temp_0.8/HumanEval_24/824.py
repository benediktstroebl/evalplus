Here's a self-contained Python function that finds the largest divisor of a given number n:
```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number divisible by n, smaller than n
    """
    return next((d for d in range(1, n+1) if n % d == 0))
```
The function uses the next() function with a generator expression to iterate through numbers from 1 to n+1. It returns the generate a largest divisor of n, which is always the next number in the sequence. The function is fully contained within the Python scope and has self-contained logic for solving the given problem.