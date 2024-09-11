```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Parameters:
    x (int): The number to be converted.
    base (int): The base to convert to.

    Returns:
    str: The string representation of x in base.

    Examples:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x == 0:
        return '0'
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    return ''.join(map(str, digits[::-1]))


# Test the function
if __name__ == "__main__":
    print(change_base(8, 3))  # Output: '22'
    print(change_base(8, 2))  # Output: '1000'
    print(change_base(7, 2))  # Output: '111'
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input, converts `x` to the base `base`, and returns the result as a string.

Here's a brief explanation of the code:

*   We first handle the case where `x` is 0, in which case we return '0'.
*   We then enter a loop where we continuously divide `x` by `base` and append the remainder to the list `digits`.
*   Once `x` becomes 0, we reverse the list `digits` (because we appended the digits in reverse order) and join them together into a string.
*   We use the `map` function to convert each digit in the list to a string, and then join them together using the `join` method.
*   Finally, we test the function by calling it with some examples.