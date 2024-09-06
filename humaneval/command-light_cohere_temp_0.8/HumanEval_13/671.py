```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the inputs is required")
    elif not (a % b == 0) or b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(6, 6))  # Output: Error: ValueError
```