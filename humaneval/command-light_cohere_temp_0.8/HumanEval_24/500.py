Here is a Python script that defines a function, largest_divisor, which finds the largest integer dividing a given number evenly, smaller than the given number n. 

```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number that divides n evenly, smaller than n
    """
    return next(i for i in range(1, n+1) if n % i == 0)
```