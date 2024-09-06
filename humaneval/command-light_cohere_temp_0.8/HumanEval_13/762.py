```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both inputs must be positive numbers")
    return math.abs(b) //: b / a
``` 
This script defines a function greatest_common_divisor that calculates and returns the greatest common divisor of two integers a and b. The function uses the mathematical operations and the built-in function math.abs() for handling negative numbers and raising a ValueError for invalid inputs.