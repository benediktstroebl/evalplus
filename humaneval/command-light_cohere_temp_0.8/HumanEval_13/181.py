```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0:
        return 0
    elif b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b) + 1

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(58, 41)))  # Output: 41
print(greatest_common_divisor(0, 4))  # Output: 0
print(greatest_common_divisor(1345, 234))  # Error: Division by zero
```