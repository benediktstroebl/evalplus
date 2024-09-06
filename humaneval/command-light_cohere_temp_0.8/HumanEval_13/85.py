```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of inputs must be a positive integer")
    return max(x for x in range(1, min(a, b)) if a % x == 0 and b % x == 0)
```
This code defines a function greatest_common_divisor that calculates and returns the greatest common divisor of two numbers a and b. It uses efficient range-based iteration with the minimum of the two numbers to check divisibility, and returns the largest of those divisors. The function raises a wrong input ValueError if at least one of the inputs is not a positive integer.