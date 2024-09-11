```python
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Use the Euclidean algorithm to find the GCD
    while b:
        a, b = b, a % b
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script defines a `greatest_common_divisor` function that takes two integers `a` and `b` as input and returns their greatest common divisor (GCD) using the Euclidean algorithm. The script then demonstrates the function with two example test cases. 

The Euclidean algorithm is a simple and efficient method for calculating the GCD of two numbers. It works by repeatedly replacing `a` and `b` with `b` and the remainder of `a` divided by `b`, until `b` is zero. At that point, `a` is the GCD. 

Note: The `>>>` lines are docstrings and don't affect the code execution. They are used to display expected output of the function when it's run with specific inputs.