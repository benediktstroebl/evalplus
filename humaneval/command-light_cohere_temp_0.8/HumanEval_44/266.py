```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base
    Returns string representation after base conversion.
    """
   
    received parameters:
        x: The number to be converted
        base: The numerical base to convert to
    """
    # perform the conversion
    num = x
    while base > 0:
        num = num // base
    # create the string representation of the number using the specified base
    result = ['0'] * (base - num + 1) + [str(num)]
    return result[::-1]

# test cases
print(change_base(8, 3))  # expected output: '22'
print(change_base(8, 2))  # expected output: '1000'
print(change_base(7, 2))  # expected output: '111'
```
This code defines a function called change_base that takes two parameters: x, representing the number to be converted, and base, representing the numerical base to convert to. 
The function performs the conversion of x to a string representation using the specified base. The idea is similar to the standard mathematical formula of converting a number to a string using a given base. 

The function uses a while loop to repeatedly divide the number by powers of the base until the base becomes zero. 

After the loop, the function creates the string representation of the number using the specified base. It does this by creating a list of zeros with a length equal to the difference between the base and the number to be converted, and then adding the number to the list. 

The function then returns the resulting string.