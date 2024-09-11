### Numerical Base Converter Script
```markdown
### Description
A Python script that converts an integer from base 10 to any base less than 10.

### Code
```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Args:
    x (int): The number to be converted.
    base (int): The base to convert to.

    Returns:
    str: String representation of the number in the given base.
    """
    if not isinstance(x, int) or not isinstance(base, int):
        raise ValueError("Both x and base must be integers.")
    if not 2 <= base <= 9:
        raise ValueError("Base must be between 2 and 9 (inclusive).")

    if x < base:
        return str(x)

    result = ''
    while x > 0:
        x, remainder = divmod(x, base)
        result = str(remainder) + result

    return result


### Example Use Cases
if __name__ == "__main__":
    print(change_base(8, 3))  # Output: '22'
    print(change_base(8, 2))  # Output: '1000'
    print(change_base(7, 2))  # Output: '111'
```

### Explanation
This script defines a function `change_base` that takes an integer `x` and a base `base` as input, and returns the string representation of `x` in the given base.

It first checks if both `x` and `base` are integers and if `base` is within the valid range (2-9). If either condition is not met, it raises a `ValueError`.

The function then uses a while loop to repeatedly divide `x` by `base` and append the remainder to the result string. This process continues until `x` becomes 0.

Finally, the script includes example use cases to demonstrate the function's usage.