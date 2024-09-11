```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to calculate the GCD.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Ensure a is the larger number
    if b > a:
        a, b = b, a
    
    # If b is zero, the GCD is a
    if b == 0:
        return a
    
    # Otherwise, recursively call the function with b and the remainder of a divided by b
    else:
        return greatest_common_divisor(b, a % b)


# Test cases
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Expected output: 1
    print(greatest_common_divisor(25, 15))  # Expected output: 5
    print(greatest_common_divisor(48, 18))  # Expected output: 6
    print(greatest_common_divisor(101, 103))  # Expected output: 1
```

This Python script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as input and returns their greatest common divisor (GCD). The function uses the Euclidean algorithm to calculate the GCD. The script also includes test cases to verify the correctness of the function.