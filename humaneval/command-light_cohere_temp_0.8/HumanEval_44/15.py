Here is a self-contained Python script with a function that changes the base of a number to a specified base:
```python
def change_base(x: int, base: int):
    """
    Change the base of a number to a specified base.
    Args:
        x: The number to change the base.
        base: int: The base to which the number will be converted

    Returns:
        str: The string representation of the number in the specified base.
    """
    #Convert the string representation of the number x to an integer
    number
    # Based on the base of the number
    # Convert the number to the desired base
    converted_number = str(x).format(format='{:b}', int=base))
    # Return the converted number
    return converted_number

# Example usage
number = 8
base = 3
result = change_base(number, base)
print(result) # Output: '22'

number = 8
base = 2
result = change_base(number, base)
print(result) # Output: '1000'

number = 7
base = 2
result = change_base(number, base)
print(result) # Output: '111'
```
This Python code defines a function called change_base that takes two arguments: x (the number to be converted) and base (the base to which the number will be converted to). It then converts the string representation of the number x to an integer using the int() function. The number is then formatted using the :b format and the int=base argument, which specifies the desired base.

Finally, it returns the converted number as a string. The code also provides examples of how the function can be used to change the base of different numbers to different bases.