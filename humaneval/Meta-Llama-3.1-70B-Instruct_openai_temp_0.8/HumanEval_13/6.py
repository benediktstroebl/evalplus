```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b
    
    This function uses the Euclidean algorithm to find the greatest common divisor.
    
    Parameters:
    a (int): The first integer
    b (int): The second integer
    
    Returns:
    int: The greatest common divisor of a and b
    
    Examples:
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Ensure a is greater than or equal to b to simplify the algorithm
    if a < b:
        a, b = b, a
    
    # If b is zero, the greatest common divisor is a
    if b == 0:
        return a
    
    # Otherwise, recursively call the function with b and the remainder of a divided by b
    else:
        return greatest_common_divisor(b, a % b)


# Test the function
print(greatest_common_divisor(3, 5))   # Output: 1
print(greatest_common_divisor(25, 15)) # Output: 5
print(greatest_common_divisor(48, 18)) # Output: 6
```

Alternatively, you can use the `math.gcd` function from Python's standard library, which is implemented in C and is generally faster than a pure Python solution:

```python
import math

def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b
    
    This function uses the math.gcd function from Python's standard library.
    
    Parameters:
    a (int): The first integer
    b (int): The second integer
    
    Returns:
    int: The greatest common divisor of a and b
    
    Examples:
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    return math.gcd(a, b)


# Test the function
print(greatest_common_divisor(3, 5))   # Output: 1
print(greatest_common_divisor(25, 15)) # Output: 5
print(greatest_common_divisor(48, 18)) # Output: 6
```