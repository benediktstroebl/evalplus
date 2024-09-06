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
``` 
The function checks for zero divisors, then uses the same approach as finding the greatest common divisor of 2 numbers to find the GCD of two numbers.