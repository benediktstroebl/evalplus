```python
def change_base(x: int, base: int):
    """
    Change the base of a number x to base b.
    :return conversion
    string representation.
    """
    expected input to be a positive integer
    :param base: int 
    :return: string representation of x converted to base b
    """
    assert isinstance(x, int)
    assert isinstance(base, int)
    assert base > 0, "base number cannot be 0"

    result = "{:b}".format(x, base)
    return result

x8 = 8
y8 = 3
z8 = 1000

# calling function with test values
print(change_base(x8, y8)) # expected output 22
print(change_base(z8, 2)) # expected output 1000
print(change_base(x8, 2)) # expected output 8
```