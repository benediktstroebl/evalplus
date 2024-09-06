```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("One or both inputs cannot be zero")
    elif a == 0 or b == 0:
        return 0
    else:
        # Calculate gcd using recursive approach
        return gcd(a, b)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(10, 55))  # Output: 5 (correct answer is 5)
print(greatest_common_divisor(1024, 1024))  # Input is now valid, return 0
```