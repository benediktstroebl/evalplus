```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    This function uses the Euclidean algorithm to find the GCD.
    The Euclidean algorithm is a way of computing the greatest common divisor (GCD) of two integers,
    based on the principle that the greatest common divisor of two numbers does not change
    if the larger number is replaced by its difference with the smaller number.

    :param a: The first integer
    :param b: The second integer
    :return: The greatest common divisor of a and b
    """
    # Ensure a is the smaller number
    if a > b:
        a, b = b, a

    # Base case: if a is 0, the GCD is b
    if a == 0:
        return b

    # Recursive case: call the function with a and the remainder of b divided by a
    return greatest_common_divisor(b % a, a)


# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

However, for large inputs, a recursive solution like this can be inefficient. Here's an iterative solution:

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    This function uses the Euclidean algorithm to find the GCD.
    The Euclidean algorithm is a way of computing the greatest common divisor (GCD) of two integers,
    based on the principle that the greatest common divisor of two numbers does not change
    if the larger number is replaced by its difference with the smaller number.

    :param a: The first integer
    :param b: The second integer
    :return: The greatest common divisor of a and b
    """
    # Ensure a is the smaller number
    if a > b:
        a, b = b, a

    # Base case: if a is 0, the GCD is b
    while a!= 0:
        b, a = a, b % a

    return b


# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

Finally, if you're using Python 3.5 or later, you can use the `math.gcd` function from the math module, which is implemented in C and is much faster than either of the above solutions:

```python
import math

def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    This function uses the math.gcd function from the math module.

    :param a: The first integer
    :param b: The second integer
    :return: The greatest common divisor of a and b
    """
    return math.gcd(a, b)


# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```