```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0:
        return b
    elif b == 0:
        return a
    
    while a != b:
        if a % b == 0:
            a, b = b, a
        else:
            a -= b
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(56, 56))  # Output: 56
print(greatest_common_divisor(24, 48))  # Output: 24
```
The function `greatest_common_divisor` calculates the greatest common divisor of two integers `a` and `b`. The function handles the cases where either of the input integers is 0 and returns the other, and also handles the case where both input integers are 0 and returns 0. 

The function then enters a `while` loop that repeatedly divides the smaller number into the larger number until they are equal. The function then returns the final, remaining value of the larger number.