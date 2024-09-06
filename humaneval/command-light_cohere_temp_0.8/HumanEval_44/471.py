```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.
    We convert a string representation of x to a string using the specified base.
    The result is : int (base)
    base is an integer
    return string representation of x using base
    """
    # ensure base is a positive integer
    if base <= 0:
        raise ValueError("base must be a positive integer")
        
    # ensure base is not equal to 10
    if base == 10:
        base = int('11')  # set a base > 10 as default
        
    # convert to string representation
    return format(x, '{0>{base}' - get the string representation of x with the specified base)

# test the function
x = 8
base = 2
result = change_base(x, base)
print(result)  # expected output: '1000'

x = 7
base = 2
result = change_base(x, base)
print(result)  # expected output: '111'

x = 10
base = 2
result = change_base(x, base)
print(result)  # expected output: '202'

x = "abc"123"
base = 2
result = change_base(x, base)
print(result)  # expected output: '22'
```
This Python code defines a function `change_base` that converts a given number `x` to a string representation using a specified base. The base is then checked to be a positive integer, and if it's not 10, it's set to 11 to ensure compatibility with other base numbers. The function uses the string formatting to represent the number with the desired base. The code then demonstrates the function with a few test cases, passing the x and base values and printing the expected output.