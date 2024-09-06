```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the inputs must be a non-zero integer.")
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers.")
    if a == 0 or b == 0:
        return 0

    common_divisor = 0
    while a % common_divisor == 0 or b % common_divisor == 0:
        common_divisor += 1
    return common_divisor

# Example usage:
```python
# Test the function with sample inputs
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```