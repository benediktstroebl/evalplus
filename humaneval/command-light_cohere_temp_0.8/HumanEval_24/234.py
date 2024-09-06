```python
def largest_divisor(n: int) -> int:
    return (n-1) // max(1, n // 2)
``` 
This Python code defines a function called largest_divisor, which takes an integer n as input and returns the largest integer that divides n exactly and returns the result. This is necessary by finding the maximum value of the floor division of n-1 by any number smaller than n, and returns the largest of these values.