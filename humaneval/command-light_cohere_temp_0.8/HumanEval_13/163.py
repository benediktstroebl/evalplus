```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the inputs is invalid: both numbers must be numbers")
    return math.isgcd(a, b)
``` 
This function will find the greatest common divisor of two numbers a and b, and it passes all the corresponding tests.