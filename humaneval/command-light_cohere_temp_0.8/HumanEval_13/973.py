```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return "Error: Input parameters must be numbers"
    if a == 0:
        return "Error: b cannot be divisible by 0"
    return max(x for x in range(1, abs(b) + 1) if not a % x)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(9, 13))  # Output: Error: Input parameters must be numbers
```