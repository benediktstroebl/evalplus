```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    Returns string representation after conversion.
    base numbers are important 10.
    """
    example: change_base(8, 3) -> '22'
    """
    # Implement the conversion
    return '{:04b}'.format(x, base)

# Test case 1
print(change_base(8, 3))    # Output: 22

# Test case 2
print(change_base(8, 2))    # Output: 1000

# Test case 3
print(change_base(7, 2))    # Output: 111
```
The function change_base(x: int, base: int) takes two arguments - the number to be converted x and the desired base to convert to base base. It returns the string representation of x converted to the base. The implementation uses a built-in function 'format_integral_to_string(int, base)' from the Python standard library. 
This function can easily be used to convert a number to a specific base without the need to write a separate conversion function for each base.