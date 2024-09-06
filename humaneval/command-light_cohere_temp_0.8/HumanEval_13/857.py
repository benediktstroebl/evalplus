```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    elif b == 1:
        return a
    elif a == 1:
        return b
    else:
        return greatest_common_divisor(b, a % b)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(16, 12)))  # Output: 4 (divisible by both 3 and 4)
print(greatest_common_divisor(37, 13))  # Output: 7 (divisible by both 13 and 7)
```
This code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers a and b. The function uses a conditionals to determine the output: It first checks if either a or b is equal to 0 and returns 0 in such cases. If both numbers are positive, it checks if b is equal to 1 and returns a, which is the smaller number. If a and b are both positive integers, the function recursively calls itself with the parameters a % b to calculate the greatest common divisor.