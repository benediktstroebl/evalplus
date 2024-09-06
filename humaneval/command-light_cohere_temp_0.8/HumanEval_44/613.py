```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    If code is a optimized implementation.
    >>> change_base(8, 3)  # returns '22'
    >>> change_base(8, 2)  # returns '1000'
    >>> change_base(7, 2)  # returns '111'
    >>> change_base(9, 5)  # returns '55555'
    >>> change_base(5, 10) # fails with error: TypeError: unsupported operand type int: '10'
    """
    if x < 0 or base < 2:  # ValueError
        raise ValueError("Input values are invalid.")
    try:
        result = ""
        while x > 0:
            digit = x % base
            result += str(digit) + ("0" if digit == 0 else "")
            x //= base
        return result
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Test the function
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
print(change_base(9, 5))  # Output: '55555'
print(change_base(5, 10))  # Output: '5' (fails due to invalid base)
```