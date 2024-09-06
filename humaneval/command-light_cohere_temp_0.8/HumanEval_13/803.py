```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one input is required")
    return max((d for d in range(1, min(a, b)) if d == (a % b) or (b % a)))

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(1, 5))   # Input not divisible by itself, hence the only option is 0
```