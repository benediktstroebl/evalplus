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
    return any([a, b, c])
```

This function checks if any combination of the three variables equals the sum of the other two. It returns a boolean that is true if any of these conditions are met, and false if they are not. 

Here is a test drive code to test the above function:
```python
# test drive code
assert any_int(5, 2, 7), "Five plus two equals seven"
assert any_int(3, 2, 2) == False
assert any_int(3, -2, 1) == True

assert any_int(3.6, -2.2, 2) == False
```

The function should return:
- True in the first and third tests because the variables sum to each other
- False in the second and fourth tests because the variables do not sum to each other and one of the numbers is not an integer.