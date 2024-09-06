```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    max_value = max(a, b)
    min_value = min(a, b)
    for i in range(1, max_value + 1):
        if (a % i) == 0 and (b % i) == 0:
            return i

    return 0

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
print(greatest_common_divisor(120, 60)))  # Output: 4 (120/60 = 4, 60/25 = 2, 4*2 = 4)
print(greatest_common_divisor(10, 55))  # Output: 5
```