Here is a Python script with a self-contained function that finds the largest divisor of a given number:
```python
def largest_divisor(n: int) -> int:
    """ Returns the largest number divisible by n, less than n itself."""
    return (n + 1) // max((i + 1) // n for i in range(1, int(n ** 0.5)))
```
This function uses the formula for finding largest divisors to calculate the largest number divisible by n that is less than n itself. 

The time complexity of this function is O(log(n)), which makes it efficient for larger inputs.