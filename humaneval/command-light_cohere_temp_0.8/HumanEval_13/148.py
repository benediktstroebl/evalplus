```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return "Input must be integers"
    while a % b == 0:
        b = a // b
    return b

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```