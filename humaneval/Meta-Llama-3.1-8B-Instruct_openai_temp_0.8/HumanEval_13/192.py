```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b
    
    This function uses the Euclidean algorithm to find the GCD.
    
    Parameters:
    a (int): The first integer
    b (int): The second integer
    
    Returns:
    int: The greatest common divisor of a and b
    """
    while b:
        a, b = b, a % b
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as input and returns their greatest common divisor (GCD). It uses the Euclidean algorithm to calculate the GCD. The script includes two test cases to demonstrate its usage.

The Euclidean algorithm is an efficient method for computing the GCD of two integers. It works by repeatedly replacing `a` and `b` with `b` and `a % b` until `b` becomes zero. At that point, `a` is the GCD. This algorithm has a time complexity of O(log min(a, b)), making it suitable for large integers.