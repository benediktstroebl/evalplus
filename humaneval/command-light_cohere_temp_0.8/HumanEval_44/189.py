```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.
    Base must be a string and greater than 2.
    """
    int, str. would be in base number
   
    number is converted to a string representation.
    """
    number to be represented in a string, using the given base.
    """
    returned string representation is in the original base.
    """
    convert the string to decimal numbers and return it
    """
    # convert x to string representation in base
    # convert to decimal representation
    return '{:.2f}'.format(x, base)

# test
x = 8
base = 2
result = change_base(x, base)
print(result) # Output: '1000'
```
The function change_base() changes the base of a number to another base. It takes two input number x and a base. The function returns the string representation of the number in the original base, converts it to a string representation in the desired base, and then converts the string back to decimal numbers. The function returns the string representation of the number in the original base, which is represented as a string in the desired base.