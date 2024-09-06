```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number x to base base.
    :return new string representation with the base
    """
    # convert x to string using expanded notation
    x = str(x)
    # adjust the number based on the base
    return format(x, f"{base}{' '}", int(x))

# test case using the function
print(change_base(8, 3)) # expected output 22
print(change_base(5, 4)) # expected output 20
print(change_base(7, 8)) # expected output 111
```