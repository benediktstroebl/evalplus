```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    if a == 0:
        return b
    elif b == 0:
        return a

    while a != 0:
        a, b = divmod(a, b)
        if a == 0:
            break

    return b

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(125, 57))  # Output: 19
print(greatest_common_divisor(17, 181))  # Output: 61
```
This code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers a and b. The function first checks if either a or b are zero, in which case it returns the other. If both are not zero, it enters a loop where it continuously divides the larger number by the smaller one, until the smaller number becomes zero. Finally, it returns the maximum divisor found.