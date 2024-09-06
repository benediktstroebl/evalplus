```python
def change_base(x: int, base: int):
    """
    Change the base numerical representation of input number x to base base.
    return string representation after conversion.
    base numbers less 10
    a decimal, binary, octal, or hexadecimal
    """
    assert isinstance(x, int) and x > 0, "Input number should be positive"
    assert isinstance(base, int) and base > 0 and base <= 16, "Base should be a positive integer less than 17"

    result = "{:0b}".format(x, base)
    return result

x = 8
base = 2
print(change_base(x, base)) # Output: 1000
x = 7
base = 2
print(change_base(x, base)) # Output: 111
x = -1
base = 10
print(change_base(x, base)) # Output: invalid input
```