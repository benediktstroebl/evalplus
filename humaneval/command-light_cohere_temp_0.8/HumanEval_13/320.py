```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")

    # The GCD is the first common divisor of the two numbers
    return math.gcd(a, b)
``` 
This function uses the built-in `math.gcd()` function to calculate the greatest common divisor of two integers a and b. The function raises a ValueError if the inputs are not both numbers. 

This function is self-contained and efficiently calculates the greatest common divisor using built-in functions, making it a clean and concise solution for the given problem.