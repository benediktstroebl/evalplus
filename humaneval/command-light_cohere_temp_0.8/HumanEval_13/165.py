```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the numbers must be provided")
    return max(math.gcd(a, b))
``` 
This function calculates the greatest common divisor of two integers a and b using the built-in `math.gcd()` function, which computes the greatest common divisor of two numbers a and b. This function also raises a ValueError exception if either number is not provided.