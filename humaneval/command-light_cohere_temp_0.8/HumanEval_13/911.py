```python
def greatest_common_divisor(a, b): 
    while b != 0:
        rem = a % b
        a = b
        b = rem
    if a > 0:
        return a
``` 

This function, `greatest_common_divisor`, calculates the greatest common divisor of two integers a and b. The function uses the specified modulus operator to determine the greatest common divisor, ensuring it always returns a positive value for a valid input.