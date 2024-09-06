```python
def largest_divisor(n: int) -> int:
    """ Returns the largest integer dividing n evenly, smaller than n."""
    return n // max(1, n % 2)
```  This function uses the floor division to ensure the result is an integer, and the `max` function to prevent division by zero.  It approach is `n % 2` to check if `n` is odd, to ensure the function only returns a number greater than one.