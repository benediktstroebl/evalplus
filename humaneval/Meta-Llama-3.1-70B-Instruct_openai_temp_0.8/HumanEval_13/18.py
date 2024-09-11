```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm, which is an efficient method for computing the greatest common divisor of two integers.

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
    print(greatest_common_divisor(3, 5))   # Output: 1
    print(greatest_common_divisor(25, 15)) # Output: 5
```

This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b` using the Euclidean algorithm. The function uses a while loop to repeatedly replace `a` with `b` and `b` with the remainder of `a` divided by `b`, until `b` becomes zero. At this point, `a` is the greatest common divisor of the original `a` and `b`.

The script also includes example usage of the `greatest_common_divisor` function, which can be run by executing the script directly (i.e., not by importing it as a module in another script).