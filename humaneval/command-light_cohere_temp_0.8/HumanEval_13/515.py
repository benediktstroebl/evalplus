```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the inputs must be a non-zero integer.")
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers.")
    if a == 0:
        return 0
    if b == 0:
        return 0
    if a == b:
        return a
    gcd = __import__('math').gcd(a, b)
    return gcd
```  This code defines a function, `greatest_common_divisor`, that calculates and returns the greatest common divisor of two integers a and b.  It implements this using the result by efficiently calculating the greatest common divisor using the `math` library's built-in `gcd` function. The function includes input validation to ensure that the inputs are non-zero integers and raise appropriate error messages for other input conditions.