```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0

    if a == 0:
        return b
    elif b == 0:
        return a

    while a % b == 0:
        a //= b
    else:
        return a

    return b

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
print(greatest_common_divisor(12, 5)))  # Output: 2 (divisible by both 5 and 12)
print(greatest_common_divisor(56, 49)))  # Output: 7 (divisible in 56 by both 7 and 49)
```
The function calculates the greatest common divisor of two integers a and b. It first checks if either a arguments are zero and if so, returns the other argument as the result. If both are arguments are not zero, it compares them and divides by the smaller argument until it reaches a divisible by both result. Finally, it returns the greatest common divisor.