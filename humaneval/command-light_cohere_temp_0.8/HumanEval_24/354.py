```python
def largest_divisor(n: int) -> int:
    """Finds the largest divisor of n that is less than n."""
    return max(range(n + 1, 0, -1), key=lambda x: x % n == 0)
```
This function uses the Python built-in `range` function and a lambda function to find the largest number that divides the number `n` evenly, i. On the `range` function, the start value is set to `n + 1` (to avoid any possible divisor of `n` itself), and the `key` parameter is set to a lambda function that returns `True` if the divisor is `0` (i.e., the also `n` evenly). 
Another interesting observation is that the `range` function doesn't actually start at negative infinity, it starts at `n + 1`.