```python
def int_to_base(n: int, base: int) -> str:
    """
    Convert integer to any base between 2 to 9.

    Args:
        n (int): Number to convert.
        base (int): Numerical base to convert to.

    Returns:
        str: String representation of number in the new base.
    """
    if n < base:
        return str(n)
    else:
        return int_to_base(n // base, base) + str(n % base)


def change_base(x: int, base: int) -> str:
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.

    Args:
        x (int): Number to convert.
        base (int): Numerical base to convert to.

    Returns:
        str: String representation of number in the new base.
    """
    return int_to_base(x, base)


# Example usage
if __name__ == "__main__":
    print(change_base(8, 3))  # Output: '22'
    print(change_base(8, 2))  # Output: '1000'
    print(change_base(7, 2))  # Output: '111'
```

This script defines a recursive function `int_to_base` to convert a given integer `n` to a string representation in a specified base. The `change_base` function simply calls `int_to_base` with the input number `x` and the desired base. The example usage at the end demonstrates the function's output for the provided test cases.