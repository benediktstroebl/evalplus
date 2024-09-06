```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```

The GCD algorithm leverages the property that the greatest common divisor persists when the larger number is replaced by the remainder of the larger number divided by the smaller number. Starting with the larger number eliminates the chance of returning 0 as a mistake. The base case is when either number is 0, where the other number is returned as the GCD.