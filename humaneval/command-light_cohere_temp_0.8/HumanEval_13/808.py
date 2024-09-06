```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        return 0

    # Calculate GCD using the Euclidean Algorithm
    while b:
        a, b = b, a % b

    return a

# Unit tests
assert(greatest_common_divisor(3, 5)) == 1
assert(greatest_common_divisor(25, 15)) == 5
assert(greatest_common_divisor(10, 25)) == 5
assert(greatest_common_divisor(56, 56)) == 56
```
This code defines a function greatest_common_divisor that calculates the greatest common divisor of two numbers a and b. It utilizes the process that repeatedly calculates the remainder of a division of b by a until b becomes 0. The function returns the value of the greatest common divisor, which is the argument a in this case.