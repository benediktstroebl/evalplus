```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.
    
    This function uses the Euclidean algorithm, which is an efficient method 
    for computing the greatest common divisor of two integers.

    Args:
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

    # Ensure a is the larger number to simplify the algorithm
    if b > a:
        a, b = b, a

    # Base case: if b is zero, the GCD is a
    if b == 0:
        return a

    # Recursive case: call the function with b and the remainder of a divided by b
    else:
        return greatest_common_divisor(b, a % b)


# Test the function
print(greatest_common_divisor(3, 5))   # Output: 1
print(greatest_common_divisor(25, 15)) # Output: 5
print(greatest_common_divisor(48, 18)) # Output: 6
```

Alternatively, you can also use a loop instead of recursion to implement the Euclidean algorithm:

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm, which is an efficient method 
    for computing the greatest common divisor of two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.
    """

    # Ensure a is the larger number to simplify the algorithm
    if b > a:
        a, b = b, a

    while b!= 0:
        a, b = b, a % b

    return a

# Test the function
print(greatest_common_divisor(3, 5))   # Output: 1
print(greatest_common_divisor(25, 15)) # Output: 5
print(greatest_common_divisor(48, 18)) # Output: 6
```