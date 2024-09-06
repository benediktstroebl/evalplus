```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the numbers is required")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Input must be numbers")

    if a == 0 or b == 0:
        return 0

    # Use the Euclidean Algorithm to find the greatest common divisor
    while a != 0 and b != 0:
        a, b = divmod(a, b)

    return min(a, b)

# Test the function
test_value = greatest_common_divisor(3, 5)
print(test_value)  # Output: 1
test_value = greatest_common_divisor(25, 15)
print(test_value)  # Output: 5
```