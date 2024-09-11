```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the GCD.
    The Euclidean algorithm is based on the principle that the greatest common divisor of two numbers
    does not change if the larger number is replaced by its difference with the smaller number.

    :param a: The first integer
    :param b: The second integer
    :return: The greatest common divisor of a and b
    """
    while b!= 0:
        # Replace 'a' with 'b' and 'b' with the remainder of 'a' divided by 'b'
        a, b = b, a % b
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that takes two integers as input and returns their greatest common divisor. It uses the Euclidean algorithm to calculate the GCD. The function includes a docstring that describes what the function does, what parameters it takes, and what it returns. The script also includes some test cases to demonstrate the function's usage.