```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.
    
    The greatest common divisor (GCD) of two integers a and b is the largest positive integer that divides both a and b without leaving a remainder.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The greatest common divisor of a and b.
    
    Examples:
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    # Base case: If b is zero, the GCD is a
    if b == 0:
        return a
    
    # Recursive case: The GCD of a and b is the same as the GCD of b and the remainder of a divided by b
    else:
        return greatest_common_divisor(b, a % b)


# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script uses the Euclidean algorithm to calculate the greatest common divisor of two integers. The Euclidean algorithm is based on the principle that the greatest common divisor of two numbers does not change if the larger number is replaced by its difference with the smaller number. This process is repeated until the two numbers become equal, which is the greatest common divisor.

The time complexity of this algorithm is O(log min(a, b)), where a and b are the input integers. This is because with each recursive call, the algorithm effectively divides the larger number by the smaller number, reducing the problem size by at least half each time.