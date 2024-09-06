```python
def largest_divisor(n: int) -> int:
    return n // max([1] + 4)
``` 
This Python function named `largest_divisor` calculates and returns the largest integer that divides the given `n` evenly, ensuring it's smaller than the input number. The function leverages the value of `1` and `4` as the largest integers that can evenly divide `n`, and then it uses the `max` function to find the maximum of these values, which gives the largest divisor.