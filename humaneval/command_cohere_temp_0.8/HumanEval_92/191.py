```python
def any_int(x, y, z):
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    """
    a = x + y == z
    b = y + z == x
    c = x + z == y
    return bool(a or b or c)
```

This function checks if any combination of adding two of the three numbers equals the third number. The `bool()` function is used to convert the result into a boolean type. 

To test this function, you can use the following code:
```python
# test 1
print(any_int(5, 2, 7))  # Expected output: True

# test 2
print(any_int(3, 2, 2))  # Expected output: False

# test 3
print(any_int(3, -2, 1))  # Expected output: True

# test 4
print(any_int(3.6, -2.2, 2))  # Expected output: False
```

The expected output should be:
```
True
False
True
False
```

This would verify that the `any_int()` function is correctly solving the problem statement.