### Greatest Common Divisor (GCD) using Euclidean Algorithm
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    The Euclidean algorithm is used to find the GCD.
    It's based on the principle that the greatest common divisor of two numbers
    does not change if the larger number is replaced by its difference with the smaller number.

    :param a: First integer
    :param b: Second integer
    :return: Greatest common divisor of a and b
    """
    # Base case: If b is 0, the gcd is a
    if b == 0:
        return a
    # Recursive case: Replace a by b and b by the remainder of a divided by b
    else:
        return greatest_common_divisor(b, a % b)


# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```
This script uses the Euclidean algorithm to find the GCD of two integers `a` and `b`. The algorithm works by repeatedly replacing the larger number by its difference with the smaller number, until the two numbers are equal (which is the GCD). The script includes two test cases to verify that the function works correctly.