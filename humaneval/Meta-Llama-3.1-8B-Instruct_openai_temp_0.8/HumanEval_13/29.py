```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b
    
    :param a: The first integer
    :type a: int
    :param b: The second integer
    :type b: int
    :return: The greatest common divisor of a and b
    :rtype: int
    """
    
    # Use the Euclidean algorithm to find the GCD
    while b:
        a, b = b, a % b
    
    # The GCD is the last non-zero remainder
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script uses the Euclidean algorithm to find the greatest common divisor of two integers. The Euclidean algorithm is an efficient method for computing the GCD of two numbers, and it works by repeatedly dividing the larger number by the smaller one until the remainder is zero. The last non-zero remainder is the GCD.