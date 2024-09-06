```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    return math.isgcd(a, b)
```
Now, you have a function gcd that calculates the greatest common divisor of two numbers a and b.

This function uses the built-in math.isgcd() function to efficiently compute the greatest common divisor. The function raises a ValueError exception if either a or b is None or not a number.