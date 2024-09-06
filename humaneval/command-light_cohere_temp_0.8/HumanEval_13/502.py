```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    if a == 0:
        return b
    elif b == 0:
        return a

    while b != 0:
        a, b = b, a % b

    return b

# Test the function
# Introduce variables for a and b values
a = 25
b = 15

print(greatest_common_divisor(a, b))  # Output: 5
```