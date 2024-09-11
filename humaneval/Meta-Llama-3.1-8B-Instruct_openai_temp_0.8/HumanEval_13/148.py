```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    The greatest common divisor (GCD) of two integers is the largest positive integer
    that divides each of the integers without leaving a remainder.

    :param a: First integer
    :param b: Second integer
    :return: The greatest common divisor of a and b
    """
    while b!= 0:
        a, b = b, a % b
    return abs(a)


# Test cases
print(greatest_common_divisor(3, 5))  
print(greatest_common_divisor(25, 15))  
print(greatest_common_divisor(12, 18)) 
```
This script implements the greatest common divisor function using the Euclidean algorithm, which is an efficient method for finding the GCD of two integers. The function iteratively applies the remainder operation until one of the numbers becomes zero, at which point the other number is the GCD. The `abs` function is used to ensure the GCD is always positive. The test cases demonstrate the function's usage with different inputs.