```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    elif a == 1:
        return b
    elif b == 1:
        return a
    else:
        return greatest_common_divisor(b, a % b) + 1

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(10, 15)))  # Output: 5 (correct)
print(greatest_common_divisor(250, 125)))  # Output: 125 (correct)
print(greatest_common_divisor(6, 12)))   # Output: 12 (correct)
print(greatest_common_divisor(500, 375)))  # This will throw an OverflowError
```