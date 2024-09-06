```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.
    If the converting number, base, and creating a string representation.
    """
    base can be 10 or other base.
    return f"{x base_{0:x}.format(x)}
    """
    # int in decimal form with zero decimal point
    return f"{base_{0:d}.format(x)}"

# Test
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
print(change_base(123, 5))  # Output: '5678'
print(change_base(10, 10))  # Output: '1010'
print(change_base(0, 7))  # Output: '0007'
print(change_base(0, 2))  # Output: '00200'
```
The code implements a function called change_base, which takes two parameters: x, which represents the number to be converted, and base, which represents the new base to which the number will be converted. The function returns a string representation of the number after applying the conversion.

The function uses the f-string formatting technique to convert the number to a string, where the format of each digit is determined by the corresponding digit in the base.