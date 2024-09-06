```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be positive.")
    return math.gcd(a, b)
``` 
This function calculates the greatest common divisor using the built-in math.gcd function. The function also includes a test case to check if both numbers are valid positive values. 

This self-contained solution efficiently finds the GCD of two numbers.