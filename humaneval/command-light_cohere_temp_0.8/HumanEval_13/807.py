```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    if a == 0:
        return b
    elif b == 0:
        return a

    while a % b == 0:
        a //= b

    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
print(greatest_common_divisor(9, 125)))  # Output: 25
print(greatest_common_divisor(177, 181)))  # Output: 181
```
This code defines a function `greatest_common_divisor` that computes the greatest common divisor of two given integers `a` and `b`. The function uses the `if` and `while` conditions to check for special cases and iterates until the divisor of `a` and `b` is found, returning the divisor. 
Test cases are provided at the bottom of the script, and the output for each test case is printed to the console.