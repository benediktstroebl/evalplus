```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number that divides n exactly without a remainder.
    Example:
    if n <= 0 or n %= 0:
        return 0
    return 2  # least common multiple of 2 and n-1
"""

# Test cases
 assert largest_divisor(15) == 5
 assert largest_divisor(10) == 4
 assert largest_divisor(1223) == 24 

``` 
This code defines a Python function `largest_divisor` which calculates the largest integer that divides a given number `n` without a remainder. The function first checks if `n` is less than or equal to 0, and if so, returns 0 since any number less than or equal to 0 would divide evenly. Then, it returns the common multiple of 2 and `n-1` as the largest integer divisor of n, which ensures that the result is less than n.