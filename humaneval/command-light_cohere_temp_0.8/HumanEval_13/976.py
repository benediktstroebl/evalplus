```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        return 0
    return max(d for d in range(1, min(a, b)) if a % d == 0 and b % d == 0)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(12, 57))  # Output: 1 (Only 1 works as a is less than both numbers)
```