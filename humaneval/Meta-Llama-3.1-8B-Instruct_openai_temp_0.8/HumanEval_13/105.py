### Greatest Common Divisor (GCD)
#### Problem Statement
Calculate the greatest common divisor (GCD) of two integers.

#### Solution
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The GCD is the largest number that divides both a and b without leaving a remainder.

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
    while b!= 0:
        # Euclidean algorithm: replace 'a' with 'b' and 'b' with the remainder of a / b
        a, b = b, a % b
    return abs(a)
```

#### Explanation
This function uses the Euclidean algorithm to calculate the GCD. The algorithm repeatedly replaces 'a' with 'b' and 'b' with the remainder of 'a' divided by 'b' until 'b' is 0. At this point, 'a' is the GCD. The `abs` function is used to ensure the GCD is always positive.

#### Example Usage
```python
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```