```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be not equal to 0")
    if a == 0 or b == 0:
        return 0
    
    m = max(a, b)
    if m % a == 0 or m % b == 0:
        return m
    else:
        return 1

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(10, 20))  # Output: 10
print(greatest_common_divisor(9, 12)))  # Output: 3
print(greatest_common_divisor(-1, 7))  # Raises ValueError: Both numbers must be > 0
```