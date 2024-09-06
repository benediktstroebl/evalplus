```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    a = x + y == z
    b = y + z == x
    c = x + z == y
    return a or b or c
```

This function checks if any combination of the three variables adds up to the other variable. It works with the properties of the integers and does not require any additional import. Let's verify with some test cases:
```python
# Testing a variety of inputs
print(any_int(5, 2, 7))  # Should be True
print(any_int(3, 2, 2))  # Should be False
print(any_int(3, -2, 1))  # Should be True
print(any_int(3.6, -2.2, 2))  # Should be False
```

All cases should return the expected output:
```
True
False
True
False
```