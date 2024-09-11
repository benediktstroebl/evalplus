```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the GCD.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return a

# Example usage:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as input and returns their greatest common divisor. The function uses the Euclidean algorithm, which is a simple and efficient method for computing the GCD of two numbers.

Here's a step-by-step explanation of how the function works:

1. The function takes two integers `a` and `b` as input.
2. The function enters a while loop that continues as long as `b` is not zero.
3. Inside the loop, the function swaps the values of `a` and `b` and replaces `b` with the remainder of `a` divided by `b`.
4. The loop repeats until `b` is zero.
5. At this point, `a` is the GCD of the original `a` and `b`, and the function returns this value.

The script also includes some example usage of the function to demonstrate its behavior.