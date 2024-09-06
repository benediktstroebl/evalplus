```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the inputs is not a number.")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers.")

    # Calculate the greatest common divisor using prime factorization
    gcd = 1
    while b > 0:
        rem = a % b
        a, b = b, rem
        gcd = rem
    return gcd
``` 
Do you want help with anything else?