```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)

print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(16, 24)))  # Output: 8
``` 
This script defines a recursive function `greatest_common_divisor` which computes the greatest common divisor of two integers `a` and `b`. The function handles the cases when either of the input numbers is 0 and when the inputs are equal, it uses the modulo operator to find the greatest common divisor.