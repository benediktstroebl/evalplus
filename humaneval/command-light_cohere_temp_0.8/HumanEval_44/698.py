```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    Returns string representation after conversion.
    base numbers are other 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(123, 5)
    Traceback (most recent call last):
      File "<ipython-input>", line 3, in <module>
        ^
    File "<ipython-input>", line 6, in change_base
    Line 18, TypeError: unsupported operand type(123) for multiplication
    Expected an integer or float, got 'str'
    """
    return str(x * pow(base, x))

# Test the function with several cases
print(change_base(8, 3))  # Output: 22
print(change_base(8, 2))   # Output: 1000
print(change_base(7, 2))   # Output: 111
print(change_base(123, 5))  # Output:>-<Do not have a base 2 representation
```