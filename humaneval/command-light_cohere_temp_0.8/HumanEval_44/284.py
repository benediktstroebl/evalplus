```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of integer x to base base.
    Return string representation of x with decimal points removed.
    """
   
    base numbers less than 10
    """
    # convert x to a string with no decimal points
    return ''.join(''.join(str(x), place=intored(base)) for intored in range(base))

# Test the function
print(change_base(8, 3)) # expected output '22'
print(change_base(5, 2)) # expected output '1000'
print(change_base(7, 2)) # expected output '111'
print(change_base(0, 4)) # expected output '00000000'
print(change_base(10, 4)) # expected output '000000010'
```