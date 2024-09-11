```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.
    
    This function uses the Euclidean algorithm, which is an efficient method for calculating the greatest common divisor.
    
    Args:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The greatest common divisor of a and b.
    """
    # Ensure a and b are positive
    a = abs(a)
    b = abs(b)
    
    # If b is 0, the GCD is a
    if b == 0:
        return a
    else:
        # Otherwise, recursively call the function with b and the remainder of a divided by b
        return greatest_common_divisor(b, a % b)


# Test the function
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
```

Alternatively, you could use a while loop instead of recursion to calculate the GCD:

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.
    
    This function uses the Euclidean algorithm, which is an efficient method for calculating the greatest common divisor.
    
    Args:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The greatest common divisor of a and b.
    """
    # Ensure a and b are positive
    a = abs(a)
    b = abs(b)
    
    # Continue to divide a by b and replace a with b and b with the remainder until b is 0
    while b!= 0:
        a, b = b, a % b
    
    # At this point, a is the GCD
    return a


# Test the function
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
```