```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the numbers is required")
    return math.gcd(a, b)
``` 
This function calculates the greatest common divisor using the built-in math.gcd() function from the specific testing and handling cases where at least one of the inputs is 0.