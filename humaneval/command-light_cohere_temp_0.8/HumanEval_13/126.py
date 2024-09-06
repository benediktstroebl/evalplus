```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    d, r = divmod(a, b)
    if d == 0:
        return r

    return greatest_common_divisor(b % r, r)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
print(greatest_common_divisor(36, 12)))  # Output: 4
print(greatest_common_divisor(30, 15)))  # Output: 5
```
This function `greatest_common_divisor` calculates the greatest common divisor of two integers `a` and `b`. The function uses the `divmod` function to calculate the remainder when dividing a by b. It then recursively calls the(b) % r and checks if the result is 0. The function then continues the process until the remainder becomes 0, at which point the greatest common divisor is the remainder. The function then returns the result.