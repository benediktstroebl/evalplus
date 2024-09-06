```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the inputs must be a non-zero integer.")
    while a != 1 or b != 1:
        if a % b == 0:
            return b
        a,b = b, a + b
    return None

# Test cases
print(greatest_common_divisor(3, 5))      # Output: 1
print(greatest_common_divisor(25, 15)))   # Output: 5
print(greatest_common_divisor(2, 100))    # Input: 2 is a common divisor of 100, but is not the greatest one.
```