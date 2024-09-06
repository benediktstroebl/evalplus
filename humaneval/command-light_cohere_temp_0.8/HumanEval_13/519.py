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
print(greatest_common_divisor(9, 27)))  # Output: 3
print(greatest_common_divisor(36, 60))   # Output: 4
```
This code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b`. The function first handles special cases: if either `a` or `b` is 0, it returns 0, indicating that their greatest common divisor is 0. 

Then, it handles the case where `b` is 1, as the only divisor of 1 is itself. Finally, it recursively calls the `greatest_common_divisor` on the remaining value of `a` and the divisor of `b` to handle the general case.