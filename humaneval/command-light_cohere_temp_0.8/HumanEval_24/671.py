```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number divisible by n, 
    which is less than n and a positive integer.
    """
    n = n + 1 
    while n % 2 == 0 and n != 1: 
        n += 1
    return n 
``` 
This script defines a function `largest_divisor` that finds the largest divisor of a given number `n` such that it is a positive integer, and that divides the given number evenly. The condition for incrementing the necessary number is that the number is even and greater than 1, but not equal to `n`.