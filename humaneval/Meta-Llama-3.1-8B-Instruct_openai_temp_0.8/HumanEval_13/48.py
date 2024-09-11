```python
# Define a function to calculate the greatest common divisor (GCD) of two numbers
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b

    Args:
    a (int): The first integer
    b (int): The second integer

    Returns:
    int: The greatest common divisor of a and b
    """

    # Base case: If b is zero, the GCD is a
    if b == 0:
        return a
    
    # Recursive case: Call the function with b and the remainder of a divided by b
    # The GCD of a and b is the same as the GCD of b and the remainder of a divided by b
    else:
        return greatest_common_divisor(b, a % b)


# Test the function with some examples
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script uses the Euclidean algorithm to calculate the greatest common divisor of two integers. The Euclidean algorithm is a well-known method for finding the GCD of two numbers, and it works by repeatedly applying the following rule:

*   If `b` is zero, then the GCD of `a` and `b` is `a`
*   Otherwise, the GCD of `a` and `b` is the same as the GCD of `b` and the remainder of `a` divided by `b`

This recursive approach is implemented in the `greatest_common_divisor` function, which takes two integers `a` and `b` as input and returns their GCD. The function is then tested with some examples to demonstrate its correctness.