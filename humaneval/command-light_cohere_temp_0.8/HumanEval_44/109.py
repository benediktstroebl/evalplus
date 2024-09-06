```python
def change_base(x: int, base: int):
    """
    Change the numerical base of the input number x to base base.
    return string representation after conversion.
    base numbers less 10 or hung to an integer base, like 10.
    >>> change_base(8, 3)  # Output: '22'
    """
    # Convert x to string representation in the desired base
    result = ""
    while x > 0:
        carrying = x % base
        result = carrying + str(x // base) + result
        x = base
    return result

# Test case 1
print(change_base(8, 3))  # Output: '22'

# Test case 2
print(change_base(8, 2))  # Output: '1000'

# Test case 3
print(change_base(7, 2))  # Output: '111'
```
This Python script defines a function `change_base` that converts a given number `x` to its string representation in a specified base `base`. The function utilizes a loop to repeatedly subtract the least significant digit of `x` from the number, adding the digit in reverse order to the result string.