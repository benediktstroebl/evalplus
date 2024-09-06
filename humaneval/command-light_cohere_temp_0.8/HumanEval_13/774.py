Here is a Python script that includes the function `greatest_common_divisor` which calculates and returns the greatest common divisor of two integers `a` and `b` : 

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return the greatest common divisor of a and b """
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return greatest_common_divisor(b, a%b)

print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
``` 

This function will return the greatest common divisor of the numbers a and b. A conditional check is the check if either of the numbers are equal to zero, which means they are not valid inputs for the function, and it will return the other number as the greatest common divisor.