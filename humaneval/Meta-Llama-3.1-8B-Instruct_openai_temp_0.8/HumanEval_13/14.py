```python
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    """
    
    # Base case: If b is zero, the gcd is a
    if b == 0:
        return a
    
    # Recursive case: Replace 'a' with 'b' and 'b' with the remainder of a divided by b
    else:
        return greatest_common_divisor(b, a % b)

# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script uses the Euclidean algorithm to find the greatest common divisor (GCD) of two integers. The Euclidean algorithm is an efficient method for computing the GCD of two numbers, and it works by repeatedly replacing 'a' with 'b' and 'b' with the remainder of a divided by b, until b is zero. At that point, a is the GCD.