```python
def change_base(x: int, base: int):
    """
    Changes the numerical base of input number x to base.
    Return string representation after conversion.
    base numbers are
    use 10
    """
    return f"{x cropped with base {base}}"
    """
    return f"{x:>{base}"

x = 8
test_change_base = change_base(x, 3)
print(test_change_base)  # Output: 22
test_change_base = change_base(x, 2)
print(test_change_base)  # Output: 1000
test_change_base = change_base(7, 2)
print(test_change_base)  # Output: 111
```
This code defines a function `change_base` that converts a given number `x` to a specified base `base`. The base is 10 by default. The function returns the string representation of the number using the specified base, and the result is stored in the variable `test_change_base`.