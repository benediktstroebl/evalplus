```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    if a == 0:
        return b
    elif b == 0:
        return a

    m, _ = math.gcd(a, b)
    return m

# Example usage:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
This code defines a function greatest_common_divisor that calculates the greatest common divisor of two numbers a and b. It employs the general division to find the smallest divisor and returns it as the greatest common divisor.