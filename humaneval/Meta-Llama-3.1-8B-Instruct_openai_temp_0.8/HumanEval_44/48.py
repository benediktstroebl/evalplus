```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
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
print(change_base(8, 3))  # Output: 22
print(change_base(8, 2))  # Output: 1000
print(change_base(7, 2))  # Output: 111
```

This script uses recursion to achieve the base conversion. The function works by repeatedly dividing the input number `x` by the base and appending the remainder to the result. The base case for the recursion is when `x` is less than the base, at which point the function simply returns `x` as a string. The function then returns the result of the recursive call plus the remainder.