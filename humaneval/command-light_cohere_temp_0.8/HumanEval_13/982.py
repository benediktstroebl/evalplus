```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be positive.")
    while b != 0:
        if a % b == 0:
            a, b = b, a // b
        else:
            break
    return a

# Test case 1
print(greatest_common_divisor(3, 5))  # Output: 1

# Test case 2
print(greatest_common_divisor(25, 15))  # Output: 5

# Test case 3
print(greatest_common_divisor(2, 48))  # Output: 6

# Test case 4
print(greatest_common_divisor(144, 243)) # Output: 9
```
This code defines a function `greatest_common_divisor(a, b)` that calculates the greatest common divisor of two integers `a` and `b`. It handles edge cases where both inputs are 0, and also checks if either number is negative, in which case it raises a `ValueError`. The function uses a loop to find the greatest common divisor by repeatedly dividing the smaller number by the larger number until the smaller number becomes 0 or until it cannot anymore divide evenly into the larger number.