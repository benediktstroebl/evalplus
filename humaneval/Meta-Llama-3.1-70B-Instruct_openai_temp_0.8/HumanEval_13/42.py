### Greatest Common Divisor (GCD) in Python
#### Using the Euclidean Algorithm

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the GCD.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return abs(a)


# Example usage:
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
    print(greatest_common_divisor(48, 18))  # Output: 6
```

This Python script defines a function `greatest_common_divisor` that takes two integers as input and returns their greatest common divisor using the Euclidean algorithm. The algorithm works by repeatedly applying the division algorithm, swapping the remainder with the divisor until the remainder is zero. The last non-zero remainder is the GCD. The result is returned as an absolute value to handle cases where the input integers are negative.