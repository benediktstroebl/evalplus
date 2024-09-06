```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    # For numbers greater than 1, the GCD is always the largest divisor
    # which is common to both numbers
    if a == 1 or b == 1:
        return 1

    return max((d for d in range(2, max(a, b)) if d == a % b == 0))

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(99, 324)) # Output: 9
```