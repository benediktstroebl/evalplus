```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    m, _ = max(a, b), 0
    for i in range(1, int(math.sqrt(max(a, b)) + 1)):
        if a % i == 0 and b % i == 0:
            m = i

    return m

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(125, 1050))  # Output: 250
print(greatest_common_divisor(15, 15))  # Output: 15
```