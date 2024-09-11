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

# Example usage
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
```

In this script, the `greatest_common_divisor` function takes two integers `a` and `b` as input and returns their greatest common divisor. The function uses the Euclidean algorithm to find the GCD.

Here's a step-by-step breakdown of how the function works:

1.  The function takes two integers `a` and `b` as input.
2.  The `while` loop continues until `b` becomes zero.
3.  Inside the loop, the function swaps the values of `a` and `b` and then updates `b` to be the remainder of `a` divided by `b` (i.e., `a % b`).
4.  Once `b` becomes zero, the function returns the value of `a`, which is the greatest common divisor of the original `a` and `b`.

The `if __name__ == "__main__":` block provides example usage of the `greatest_common_divisor` function, demonstrating how to call it with different inputs and print the results.