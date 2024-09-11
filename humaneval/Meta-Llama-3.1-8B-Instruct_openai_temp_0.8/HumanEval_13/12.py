### Greatest Common Divisor (GCD) Using the Euclidean Algorithm

Here is a Python function that calculates the greatest common divisor (GCD) of two integers using the Euclidean algorithm.

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The GCD of two integers a and b is the largest positive integer that divides both a and b without leaving a remainder.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    while b:
        # Swap a and b
        a, b = b, a % b

    return a


# Example usage:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

### Explanation:

1. We use a simple iterative approach based on the Euclidean algorithm.
2. The algorithm starts with two integers: `a` and `b`.
3. In each iteration, it replaces `a` with `b` (which is the remainder of `a` divided by `b`) and `b` with the previous value of `a`.
4. This process continues until `b` becomes zero.
5. At this point, `a` is the GCD of the original `a` and `b`.

This function uses the modulo operator (`%`) to efficiently compute the remainder of `a` divided by `b` in each iteration.

### Time Complexity:

The time complexity of this function is O(log min(a, b)), which is the number of iterations required to find the GCD.

### Space Complexity:

The space complexity of this function is O(1), as it only uses a constant amount of space to store the variables `a` and `b`.