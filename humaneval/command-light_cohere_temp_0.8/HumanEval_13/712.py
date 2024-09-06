```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    if a == 0:
        return b
    elif b == 0:
        return a

    # Use the Euclidean algorithm
    while b != 0:
        a, b = b, a % b

    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
print(greatest_common_divisor(9, 81)))  # Output: 3
```
This code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two numbers `a` and `b`. The function uses the Euclidean algorithm to efficiently find the greatest common divisor. The test cases demonstrate the the greatest common divisor for various pairs of integers. The function handles the process with two integers and returns the greatest common divisor of those numbers.