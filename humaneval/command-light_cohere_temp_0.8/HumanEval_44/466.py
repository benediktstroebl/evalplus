```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers less 10
    easy
    return a string representation
    """
    return f'{x:{base}'}'.format(base)

# Test cases
print(change_base(8, 3))  # Expected output: '22'
print(change_base(8, 2))  # Expected output: '1000'
print(change_base(7, 2))  # Expected output: '111'
```
This Python script defines a function `change_base` that converts a given number `x` to a string representation using the specified base. The test cases ensure the + valid input values and base numbers are passed, and the expected output is printed to verify the correctness of the function.