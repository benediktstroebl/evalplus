```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.
    
    This function uses the Euclidean algorithm to find the greatest common divisor.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The greatest common divisor of a and b.
    """
    # Ensure a and b are positive
    a = abs(a)
    b = abs(b)
    
    # If b is zero, the greatest common divisor is a
    if b == 0:
        return a
    
    # Otherwise, recursively call the function with b and the remainder of a divided by b
    else:
        return greatest_common_divisor(b, a % b)


# Test the function
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))   # Expected output: 1
    print(greatest_common_divisor(25, 15)) # Expected output: 5
    print(greatest_common_divisor(48, 18)) # Expected output: 6
```

In this script, the `greatest_common_divisor` function calculates the greatest common divisor of two integers `a` and `b` using the Euclidean algorithm. It first ensures that both `a` and `b` are positive, then recursively applies the Euclidean algorithm until `b` is zero. At this point, `a` is the greatest common divisor. The script includes test cases at the end to verify its correctness.