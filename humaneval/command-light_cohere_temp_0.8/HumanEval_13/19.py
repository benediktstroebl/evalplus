```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Cannot calculate GCD of zero or negative numbers")
    return math.gcd(a, b)
``` 
This function, `greatest_common_divisor`, calculates the greatest common divisor of two integers `a` and `b` using the built-in `math.gcd()` function.  It  Also has a method, it first checks for division by zero and raises a `ValueError` if either input number is zero. 
Then, it uses the `math.gcd()` function, which calculates the greatest common divisor of the two numbers.