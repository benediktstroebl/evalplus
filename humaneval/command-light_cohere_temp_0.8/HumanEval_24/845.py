```python
def largest_divisor(n: int) -> int:
    """
    Return the largest integer dividing n evenly, 
    excluding n itself.
    """
    calculate all divisors except 1 until 
    the square root of n, then take the largest.
    """
```
 ``` largest_divisor(15)  # Output: 5

This code defines a function `largest_divisor` which calculates the largest integer that divides a given number `n` evenly, excluding `n` itself. The function calculates all divisors up to the square root of `n` and then takes the largest one.