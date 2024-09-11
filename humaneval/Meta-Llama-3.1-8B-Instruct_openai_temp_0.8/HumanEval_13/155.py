```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b
    
    This function uses the Euclidean algorithm to compute the GCD.
    
    Parameters:
    a (int): The first integer
    b (int): The second integer
    
    Returns:
    int: The greatest common divisor of a and b
    """
    while b!= 0:
        # In each iteration, we replace 'a' with 'b' and 'b' with the remainder of 'a' divided by 'b'
        a, b = b, a % b
    
    return abs(a)

# Test cases
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Expected output: 1
    print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This Python function calculates the greatest common divisor (GCD) of two integers, `a` and `b`, using the Euclidean algorithm. The Euclidean algorithm works by repeatedly replacing `a` with `b` and `b` with the remainder of `a` divided by `b`, until `b` is zero. At that point, `a` is the GCD. The function returns the absolute value of `a` in case the GCD is negative.