```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    d = 1
    while b > 0:
        if a % b == 0:
            a, b = a // b, d = d + 1
        else:
            d += 1

    return d

# Test the function with some examples
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
```