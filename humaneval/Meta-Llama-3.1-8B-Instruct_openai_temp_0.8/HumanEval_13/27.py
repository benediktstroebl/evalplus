```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b
    :param a: The first integer
    :param b: The second integer
    :return: The greatest common divisor of a and b
    """
    while b!= 0:
        a, b = b, a % b
    return abs(a)

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script uses the Euclidean algorithm to calculate the greatest common divisor of two integers. The Euclidean algorithm is an efficient method for computing the greatest common divisor of two integers based on the principle that the greatest common divisor of two numbers does not change if the larger number is replaced by its difference with the smaller number. This process can be repeated until the two numbers are equal, at which point the smaller number is the greatest common divisor. The absolute value of the result is returned, to ensure the GCD is always positive. 

This script is a self-contained Python solution, with the function definition and example usage included. It adheres to Python documentation standards and is readable and maintainable. 

Note: I used two test cases to demonstrate the function's usage and effectiveness. The first test case covers the case where the greatest common divisor is 1, and the second test case covers the case where the greatest common divisor is not 1.