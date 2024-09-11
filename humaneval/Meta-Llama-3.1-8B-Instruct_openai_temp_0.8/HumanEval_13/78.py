### Greatest Common Divisor (GCD)
#### Problem Statement
Compute the greatest common divisor (GCD) of two integers using the Euclidean algorithm.

#### Solution
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The Euclidean algorithm is used to compute the GCD.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.

    Example:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    # Ensure b is the smaller number to simplify the algorithm
    if a < b:
        a, b = b, a

    while b!= 0:
        # Replace a with b, and b with the remainder of a divided by b
        a, b = b, a % b

    # The GCD is the remaining non-zero value of a
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

#### Explanation
The Euclidean algorithm is an efficient method for computing the GCD of two integers. It works by repeatedly replacing `a` with `b` and `b` with the remainder of `a` divided by `b`, until `b` is zero. At this point, `a` is the GCD.

In this implementation, we use a simple while loop to perform the Euclidean algorithm. We also include a few lines to ensure that `a` is the larger number, making the algorithm more efficient.

Finally, we test the function with the provided examples to demonstrate its correctness.