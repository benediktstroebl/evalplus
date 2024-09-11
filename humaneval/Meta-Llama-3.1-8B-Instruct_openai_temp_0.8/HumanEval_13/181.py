### Greatest Common Divisor (GCD) Calculator
#### Using the Euclidean Algorithm

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b!= 0:
        # Swap 'a' and 'b' and take the remainder of 'b' divided by 'a' as 'b'
        a, b = b, a % b
    return abs(a)

# Example usage
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script implements the Euclidean algorithm, an efficient method for calculating the greatest common divisor (GCD) of two integers. The `greatest_common_divisor` function takes two integers `a` and `b` as input and returns their GCD. The function uses a while loop to repeatedly apply the Euclidean algorithm until `b` equals 0, at which point `a` is the GCD. The `abs` function is used to ensure the result is always non-negative.