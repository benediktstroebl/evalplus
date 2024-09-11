```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b
    
    This function uses the Euclidean algorithm, which is an efficient method 
    for computing the greatest common divisor of two integers.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The greatest common divisor of a and b.
    """
    while b!= 0:
        # Swap the values of a and b
        a, b = b, a % b
    
    return abs(a)

# Test cases
print(greatest_common_divisor(3, 5))   # Expected output: 1
print(greatest_common_divisor(25, 15)) # Expected output: 5
```

This script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as input and returns their greatest common divisor. It uses the Euclidean algorithm to achieve this. The algorithm works by repeatedly dividing the larger number by the smaller one and taking the remainder, until the remainder is zero. At this point, the non-zero remainder is the greatest common divisor.

The function includes a docstring that explains its purpose, parameters, and return value. It also includes two test cases to demonstrate its usage. The `abs` function is used to ensure the result is always positive, even if the inputs are negative.