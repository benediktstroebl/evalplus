```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Both inputs must be positive numbers")
    return max(Math.else()(a / b, b / a))

```
This code defines a function greatest_common_divisor that calculates the greatest common divisor of two positive numbers a and b. It also includes input validation to ensure both inputs are positive numbers. 

The function uses the built-in function max() with the combination of the built-in function Math() to calculate the gcd of the two numbers. The use of the to find the maximum of the gcd of the two numbers, which is the greatest common divisor.