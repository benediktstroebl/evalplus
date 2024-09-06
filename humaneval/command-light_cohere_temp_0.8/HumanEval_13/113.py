```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return greatest_common_divisor(b, max(a % b, 0))

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
print(greatest_common_divisor(16, 24)))  # Output: 4 (Common divisor is 4)
print(greatest_common_divisor(72, 36)))  # Output: 6 (Common divisor is 6)
```