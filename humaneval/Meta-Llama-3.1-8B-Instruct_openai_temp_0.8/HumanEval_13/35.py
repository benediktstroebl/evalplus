### Greatest Common Divisor Calculation
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    This function uses the Euclidean algorithm, a well-known method for computing the GCD of two numbers.

    Args:
    a (int): The first integer
    b (int): The second integer

    Returns:
    int: The greatest common divisor of a and b
    """
    while b:
        a, b = b, a % b
    return a

# Example usage:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
This script defines a function `greatest_common_divisor` that calculates the GCD of two integers using the Euclidean algorithm. It then demonstrates how to use this function with two example cases.