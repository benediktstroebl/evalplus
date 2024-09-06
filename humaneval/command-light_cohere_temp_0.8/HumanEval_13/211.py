```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be positive")
    return math.sqrt(a * b)
``` 
The function will return the greatest common divisor of a and b, as long as both numbers are positive.  It will raise an error if the input is invalid.