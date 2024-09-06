Here's the Python code:
```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number that divides n exactly and is smaller than n
    """
    # Get the sqrt of n as a large divisor
    return int(n ** .5)
``` 
This script defines a `largest_divisor` function that calculates the largest divisor of a given integer n, which is smaller than n and divides n exactly.  The way to achieve this, the function calculates the square root of n using the `**`. `n ** .5` expression and returns the result as the largest divisor.