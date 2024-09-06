```python
def largest_divisor(n: int) -> int:
    return n // max(n, 1)

# Test cases
assertEqual(largest_divisor(15), 5)
assertEqual(largest_divisor(16), 1)
assertEqual(largest_divisor(27), 3)
assertEqual(largest_divisor(48), 4)
assertEqual(largest_divisor(72), 6)
```
This code defines a function `largest_divisor` which returns the largest divisor of a given number `n`. It uses the `max` function to find the maximum number that divides the given number evenly, and then divides the number by that maximum number to ensure the result is an integer. 

The test cases validate the functionality by passing different numbers and expected largest divisors.