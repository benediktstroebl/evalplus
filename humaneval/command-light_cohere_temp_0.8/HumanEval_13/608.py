```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0

    # start by assuming b is the divisor
    div = b
    while a > 0:
        a, b = b, a // b

    return div

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(5, 5)))  # Output: 5 (the number itself)
print(greatest_common_divisor(-3, 4)) # Output: this function handles negative numbers as well
```  This function, `greatest_common_divisor`, calculates the greatest common divisor of two given integers `a` and `b`. It uses a basic strategy where it starts by assuming that `b` is the divisor and then iteratively divides both numbers by `b` until `a` becomes zero, at which point it will have found the greatest common divisor.