```python
def greatest_common_divisor(a, b): 
    while b != 0:
        rem = a % b
        a = b
        b = rem
    if a > 0:
        return a
``` 
This function, greatest_common_divisor, calculates the greatest common divisor of two integers a and b by iteratively finding the remainder when a is divided by b. It then makes a final adjustment by assigning the value of b to the variable a and continuing the process if the remainder is still non-zero.