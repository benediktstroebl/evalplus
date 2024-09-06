```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the inputs must be a positive integer")
    return math.gcd(a, b)
``` 
This function calculates the greatest common divisor using the built-in gcd() function from the math module, ensuring that the inputs are positive and at least one.  It is also raises a ValueError if either input is not a positive integer.