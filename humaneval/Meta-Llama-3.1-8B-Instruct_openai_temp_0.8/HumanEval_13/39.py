### Greatest Common Divisor (GCD) Calculator

Below is a Python script that calculates the Greatest Common Divisor (GCD) of two integers using the Euclidean algorithm.

```markdown
### gcd.py

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

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

    while b:
        # Swap 'a' and 'b' to ensure 'a' is the larger number
        a, b = b, a % b
    return abs(a)


# Test the function
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))   # Output: 1
    print(greatest_common_divisor(25, 15)) # Output: 5
```

### Explanation

This script defines a function `greatest_common_divisor(a, b)` that takes two integers `a` and `b` as arguments. It uses the Euclidean algorithm to calculate the GCD.

Here's how it works:

1. The loop continues until `b` becomes zero. In each iteration, `a` and `b` are swapped, and `b` is replaced by the remainder of `a` divided by `b`. This process is repeated until `b` is zero.

2. At the end of the loop, `a` will hold the GCD of the original `a` and `b`. The `abs` function is used to ensure the result is always positive.

3. The script includes two test cases at the end to demonstrate the function's usage.

To run this script, save it as `gcd.py` and execute it from the command line using `python gcd.py`. The script's output will be the GCD of the two integers you specified.