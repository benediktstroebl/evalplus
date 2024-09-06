```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    
    return max(a, b) / min(a, b) if a != b else 0

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(6, 20))  # Output: 5
print(greatest_common_divisor(28, 14))  # Output: 14
print(greatest_common_divisor(0, 5))  # Output: 0
print(greatest_common_divisor(105, 3))  # Output: 3
```