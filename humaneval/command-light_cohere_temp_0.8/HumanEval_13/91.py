```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be positive")
    return math.gcd(a, b)
``` 
This function calculates the greatest common divisor (GCD) of two numbers a and b using the built-in math.gcd function. It includes input validation to ensure that both a and b are positive, raising a ValueError exception if not.