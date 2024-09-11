```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.
    
    This function uses the Euclidean algorithm, which is a well-known method for 
    calculating the greatest common divisor of two integers.

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
    # Base case: if b is 0, the GCD is a
    if b == 0:
        return abs(a)
    
    # Recursive case: call the function with b and the remainder of a divided by b
    else:
        return greatest_common_divisor(b, a % b)


# Example usage
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))   # Output: 1
    print(greatest_common_divisor(25, 15)) # Output: 5
    print(greatest_common_divisor(48, 18)) # Output: 6
```
This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers using the Euclidean algorithm. The function is then tested with some example inputs in the `if __name__ == "__main__":` block.