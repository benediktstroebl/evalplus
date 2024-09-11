### Greatest Common Divisor (GCD) Calculation
Below is a Python script that calculates the GCD of two integers using the Euclidean algorithm.

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    The Euclidean algorithm is used to find the GCD.
    This algorithm works by repeatedly replacing (a, b) with (b, a % b) until b is zero.
    At that point, a is the GCD of the original a and b.

    Examples:
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b!= 0:
        # Replace (a, b) with (b, a % b)
        a, b = b, a % b
    return abs(a)

# Example usage
print(greatest_common_divisor(3, 5))   # Output: 1
print(greatest_common_divisor(25, 15)) # Output: 5
```

In this code:

1.  We define the `greatest_common_divisor` function that takes two integers `a` and `b` as input.
2.  The function uses a while loop to repeatedly replace `(a, b)` with `(b, a % b)` until `b` is zero.
3.  At that point, `a` is the GCD of the original `a` and `b`.
4.  The `abs` function is used to ensure the GCD is always positive.
5.  We provide example usage of the function to demonstrate its correctness.