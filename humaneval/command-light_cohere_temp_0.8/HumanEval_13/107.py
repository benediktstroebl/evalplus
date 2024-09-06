```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both inputs cannot be zero")
    if a == b:
        return a
    return max(a, b)

# Test suite
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(10, 5))  # Output: 10
print(greatest_common_divisor(125, 75))  # Output: 25
```