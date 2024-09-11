```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b!= 0:
        a, b = b, a % b
    return abs(a)

# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script uses the Euclidean algorithm to calculate the greatest common divisor of two integers. The Euclidean algorithm is an efficient method for computing the greatest common divisor of two integers, based on the principle that the greatest common divisor of two numbers does not change if the larger number is replaced by its difference with the smaller number.

Here's a step-by-step explanation of the code:

1.  Define a function called `greatest_common_divisor` that takes two integer arguments `a` and `b`.
2.  Use a while loop to repeatedly replace `a` and `b` with `b` and the remainder of `a` divided by `b` until `b` becomes 0.
3.  At that point, `a` will be the greatest common divisor of the original `a` and `b`.
4.  Return the absolute value of `a` to ensure the result is always non-negative.
5.  Test the function with two example inputs: `(3, 5)` and `(25, 15)`.