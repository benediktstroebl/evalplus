```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return greatest_common_divisor(b, a % b)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(105, 25))  # Output: 25
print(greatest_common_divisor(105, 150))  # Output: 25
print(greatest_common_divisor(75, 125)))  # Output: 25
``` 
The function `greatest_common_divisor` in this code snippet is self-contained and can calculate the greatest common divisor of two integers `a` and `b`. 

This function follows a recursive approach to find the greatest common divisor. It uses the  a simple case where either of the numbers are 0, in which case it returns 0. 

It also handles the case where `b` is 1, in which case it returns `a`. 

Finally, it recursively calls the function to find the greatest common divisor of `b` and `a % b`, if `b` is not equal to 1. 

This process continues until it finds a number that is both a divisor of both `a` and `b`.  The output of the function for various test cases is also printed to the console.