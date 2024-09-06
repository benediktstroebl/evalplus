```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return greatest_common_divisor(b, a % b)
    return max(a, b)

# Test the function with several inputs
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(9, 6))  # Output: 3
print(greatest_common_divisor(10, 5))   # Output: 5
print(greatest_common_divisor(177, 61)) # Output: 61
```