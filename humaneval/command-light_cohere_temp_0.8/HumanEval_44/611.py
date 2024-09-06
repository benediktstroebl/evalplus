```python
def change_base(x: int, base: int):
    """
    Change the base of a number x to a specified base.
    Args:
        x (int): The number to be converted
        base (int): The base to convert to
    Returns:
        str: The string representation of x in the specified base
    """
    # ensure base is a valid number
    if not isinstance(base, (int, float)) or base < 2 or base > 36:
        raise ValueError("Invalid base number")
        
    # handle negative numbers
    if x < 0:
        x = abs(x)
        
    # ensure number is an integer
    x = x % 1000000007  # convert to float to ensure integer result
    x = x * pow(base, int(x))  # Apply the conversion rule
    
    return str(x)

# Test the function
x = 8
base = 3
result = change_base(x, base)
print(result)  # expected output 22

x = 8
base = 2
result = change_base(x, base)
print(result)  # expected output 1000

x = 7
base = 2
result = change_base(x, base)
print(result)  # expected output 111
```