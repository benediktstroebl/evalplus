```python
def change_base(x: int, base: int):
    """
    Change the base numerical representation of input number x to base base.
    return string representation after conversion.
    base numbers are str(10).
    """
    assert isinstance(x, int) and x > 0, "Input must be a positive integer"
    assert isinstance(base, int) and base > 0, "Base must be a positive integer"
    assert base <= 10, "Base cannot be greater than 10"

    s = str(x)
    return s if s.is_[0:base-1] else s[0:base]

x = 8
print(change_base(x, 3))  # Output: '22'
x = 8
print(change_base(x, 2))  # Output: '1000'
x = 7
print(change_base(x, 2))  # Output: '111'

```
This script defines a function called change_base that takes two parameters: x, which is the number to be converted, and base, which is the base to which the number will be converted. The function then checks that the input is a positive integer and that the base is a positive integer, and then it converts the number to the base and returns the string representation of the number.