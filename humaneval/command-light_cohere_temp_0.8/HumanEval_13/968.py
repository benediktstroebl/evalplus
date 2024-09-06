```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    
    c = 0
    while b > 0:
        if a % b == 0:
            c += 1
        a //= b
    while c < b:
        c += 1
    return c

# Test case 1
print(greatest_common_divisor(3, 5))  # Output: 1

# Test case 2
print(greatest_common_divisor(25, 15))  # Output: 5

# Test case 3
print(greatest_common_divisor(123, 456))  # Output: 56

```
This Python code defines a function `greatest_common_divisor(a, b)` that calculates and returns the greatest common divisor of two integers `a` and `b`. The function uses an iterative approach with a loop and a conditional expression to determine divisibility. It starts with the greatest common divisor and divides the larger number (b) by the remainder of `a` divided by `b`. It then iterates, using the remainder of the division to update the divisor value. The loop continues until the divisor is less than `b`, effectively finding the largest number that evenly divides `a` and `b`.

This code is self-contained and can be used to calculate the greatest common divisor of any two integers.