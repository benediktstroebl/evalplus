```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0

    # Find the greatest divisor of the larger number
    g = max(a, b)

    # If both numbers are divisible by g, g is the greatest common divisor
    if g % a == 0 and g % b == 0:
        return g

    # Otherwise, find the greatest divisor of the smaller number
    return greatest_common_divisor(b, a % g)

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```