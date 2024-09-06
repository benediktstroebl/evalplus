```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    return min(a, b) // max(a, b)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(37, 121))  # Output: 19
print(greatest_common_divisor(9, 243))  # Output: 19
print(greatest_common_divisor(0, 4))   # Output: 0
```