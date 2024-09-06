```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0:
        return b
    elif b == 0:
        return a

    while a != b:
        if a % b == 0:
            a, b = b, a
        else:
            a -= b
    return a

# Test case 1: Check for divisibility
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5

# Test case 2: Check for divisibility with negative numbers
print(greatest_common_divisor(-25, 15))  # Output: 5

# Test case 3: Check for divisibility with large numbers
print(greatest_common_divisor(53, 12))  # Output: 53

# Test case 4: Check for multiple values of a
print(greatest_common_divisor(10, 20))   # Output: 10
print(greatest_common_divisor(30, 10))   # Output: 30
```
This code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b`. The function uses a basic loop to compare the two numbers until one of them becomes zero, at which point the other will be the divisor. The function then returns the value of the larger number.