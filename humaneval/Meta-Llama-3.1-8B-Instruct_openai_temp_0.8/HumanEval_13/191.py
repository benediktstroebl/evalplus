```python
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return abs(a)

# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script uses the Euclidean algorithm to find the greatest common divisor (GCD) of two integers. The Euclidean algorithm is a well-known method for calculating the GCD of two numbers. It works by repeatedly replacing `a` and `b` with `b` and `a % b` until `b` equals 0. At that point, `a` is the GCD. The `abs` function is used to handle negative inputs correctly. 

To run this script, save it to a file with a `.py` extension (e.g., `gcd.py`) and execute it with Python: `python gcd.py`. The test cases will print the expected outputs to the console.