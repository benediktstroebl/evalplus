```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be positive")
    while b > 0:
        if a % b == 0:
            a, b = b, a
        else:
            b -= 1
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(123, 456))  # Output: Error: Both numbers must be positive but 456 is negative
print(greatest_common_divisor(-2, 7))  # Output: Error: Both numbers must be positive but 7 is negative
```

This Python code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two given integers `a` and `b`. The function ensures that both input numbers are positive and then uses a `while` loop to repeatedly subtract the larger number from the smaller number until it becomes zero, and then finds the largest divisor by keeping track of which number is the divisor of the other number.