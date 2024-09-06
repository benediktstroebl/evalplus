```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one input is zero")
    return max((i for i in range(1, max(a, b)) if a % i == 0 and b % i == 0))

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(3, 15))   # Input: raises ValueError
print(greatest_common_divisor(6, 6))   # Input: a divisor is 2, but greater
```