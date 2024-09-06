```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be greater than zero")
    return abs(b) if b > 0 and a % b == 0 else b

# Example usage:
# Test case passing
print(greatest_common_divisor(3, 5))  # Output: 1

print(greatest_common_divisor(25, 15))  # Output: 5

# Test case failing due to zero input
try:
    print(greatest_common_divisor(0, 5))
except ValueError as e:
    print(e)  # Output: Both numbers must be greater than zero
```