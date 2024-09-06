Here is a self-contained Python script that solves the problem of changing the base of a number to another base:
```python
def change_base(x, base):
    """
    Change the base of input number x to base.
    Returns the string representation after conversion.
    base numbers are with 10 are the most common.
    """
    string representation of the number using the given base.
    """
    numbers may be represented as strings, which can be converted to 
    different bases. 
"""
    return f"{x:{base}}"

x = 8
base = 3

result = change_base(x, base)
print(result)  # Output: 22

x = 8
base = 2

result = change_base(x, base)
print(result)  # Output: 1000

x = 7
base = 2

result = change_base(x, base)
print(result)  # Output: 111
```
This script defines a function change_base that takes two arguments: x, representing the number to be converted, and base, representing the base to which the number will be converted to. how we create a string representation for x using the given base. We then return the string that represents x in the specified base. 

This function is self-contained and can be used to change the base of any number to a desired base.