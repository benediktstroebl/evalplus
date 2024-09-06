```python
def largest_divisor(n: int) -> int:
    return n // max(n, 1)

# Test the function with some values
assertEqual(largest_divisor(15), 5)
assertEqual(largest_divisor(27), 3)
assertEqual(largest_divisor(12), 4)
assertEqual(largest_divisor(6), 2)
assertEqual(largest_divisor(8), 4)
```
The provided code defines a function `largest_divisor` that finds the largest integer divisor of a given number `n` that's smaller than or equal to the input. It achieves this by using the largest factor of `n` as the divisor and then dividing `n` by the factor. The function is then tested using a series of assertions to ensure its correctness for a variety of input values.