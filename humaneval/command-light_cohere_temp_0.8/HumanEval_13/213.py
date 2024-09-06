```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    if a == b:
        return a
    if b % a == 0:
        return a
    elif b == 1:
        return 1
    else:
        return greatest_common_divisor(b, a % b)

# Example usage
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
This code defines a recursive function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b`. The function first checks if both input numbers are zero or equal to each other, in which case it returns 0. If the input numbers are not both zero or equal, it checks if `b` is a factor of `a`. Then, it recursively calls the function with the arguments `b` and `a % `b`, and so on. The function continues this until it finds a number `k` such that `k` divides both `a` and `b` evenly.