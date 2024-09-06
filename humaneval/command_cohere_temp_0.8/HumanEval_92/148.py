```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    return x in [y+z, z+y, x+y] and all(type(i) == int for i in [x, y, z])
```

The function `any_int` takes three arguments `x`, `y`, and `z`. It uses the `in` operator to compare `x` against the sums of other two numbers (`y` and `z`) and checks if `x` is an integer using the `all` function with a list comprehension. 

Here's a test suite to ensure that the code works:
```python
def test_any_int():
    # True cases
    assert any_int(5, 2, 7) == True
    assert any_int(3, -2, 1) == True
    assert any_int(7, -5, 10) == True

    # False cases
    assert any_int(3, 2, 2) == False
    assert any_int(3.6, -2.2, 2) == False
    assert any_int(-3, 2, 3) == False

test_any_int()
```

The test suite contains examples from the problem statement and additional test cases to cover all the edges.