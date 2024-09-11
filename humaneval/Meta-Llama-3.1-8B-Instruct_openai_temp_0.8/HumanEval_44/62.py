```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Args:
    x (int): The number to be converted.
    base (int): The base to which the number is to be converted.
    
    Returns:
    str: String representation of the number in the new base.
    
    Examples:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x < base:
        return str(x)
    else:
        return change_base(x // base, base) + str(x % base)


# Example usage:
if __name__ == "__main__":
    print(change_base(8, 3))  # Output: '22'
    print(change_base(8, 2))  # Output: '1000'
    print(change_base(7, 2))  # Output: '111'
    print(change_base(10, 2))  # Output: '1010'
```

This script uses recursion to perform the base conversion. The function `change_base` takes two arguments, `x` and `base`, where `x` is the number to be converted and `base` is the base to which the number is to be converted.

The function first checks if `x` is less than `base`, in which case it simply returns the string representation of `x`. If `x` is greater than or equal to `base`, the function calls itself with the quotient of `x` and `base` as the new `x` and the remainder of `x` divided by `base` as the new input. The function then appends the string representation of the remainder to the string representation of the result of the recursive call, effectively building the string representation of the number in the new base from right to left.