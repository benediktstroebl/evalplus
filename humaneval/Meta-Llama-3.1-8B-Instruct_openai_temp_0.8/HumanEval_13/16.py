### Greatest Common Divisor (GCD) Calculation
#### Using Euclidean Algorithm
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The greatest common divisor (GCD) of two integers is the largest positive integer that divides both numbers without leaving a remainder.

    :param a: The first integer.
    :param b: The second integer.
    :return: The greatest common divisor of a and b.
    """
    # Base case: If b is zero, the GCD is a
    if b == 0:
        return a
    # Recursive case: Replace (a, b) with (b, a % b)
    else:
        return greatest_common_divisor(b, a % b)

# Example usage:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
This script uses the Euclidean algorithm to calculate the greatest common divisor of two integers. The Euclidean algorithm is an efficient method for computing the GCD of two numbers, and it is based on the principle that the GCD of two numbers does not change if the larger number is replaced by its difference with the smaller number.