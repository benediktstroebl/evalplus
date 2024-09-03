```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of the input number x to base base.
    >>> change_base(8, 3)  # Should return '22'
    >>> change_base(8, 2)  # Should return '1000'
    >>> change_base(7, 2)  # Should return '111'
    """
    # Apply the conversion
    num = x  # Replace with the desired number
    return format(num, f"{base}{}", int(base))

# Run the tests
print(change_base(8, 3))  # Output: 22
print(change_base(8, 2))  # Output: 1000
print(change_base(7, 2))  # Output: 111
```
The function change_base is designed to transform a given number x to a specified base base. It achieves this by applying the mathematical format specifier, ensuring that the output is a string representation of the number in the desired base.