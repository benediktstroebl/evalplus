```python
def change_base(x: int, base: int):
    """
    Change the base of integer input x to base base.
    If returns the impact on a different base number, please feel free to test!
    """
    # we convert the input to a string so we can manipulate it
    x = str(x)
    
    # we create the result string, the original base number multiplied by x divided by base number
    result = str(int(x) * int(x, base) // int(base))
    
    # we return the result string
    return result

# we run some tests on the function
print(change_base(8, 3))  # expected output 22
print(change_base(7, 5))  # expected output '007'
print(change_base(123, 10)) # expected output '12345'
print(change_base(10, 10))  # expected output '1010'
```