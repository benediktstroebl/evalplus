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
    return bool(a or b or c)
```

This function checks if any combination of adding two of the three numbers equals the third number. The `bool()` function is used to convert the result into a boolean type, which returns `True` if any of the conditions are `True`. 

Here is a test drive code to test the functionality of the function:
```python
test_drive = [
    (5, 2, 7, True),
    (3, 2, 2, False),
    (3, -2, 1, True),
    (3.6, -2.2, 2, False)
]

for entry in test_drive:
    assert any_int(*entry[0:4]) == entry[3]
```

The test drive consists of four tuples. Each tuple contains three elements (x, y, z) along with the expected outcome for the function `any_int(*entry[0:4])`. The `*entry[0:4]` unpacks the three-element tuples into arguments, allowing us to evaluate the function with different inputs. The `assert` statement checks if the output of the function is equal to the expected output, and if so, the test passes. If the test fails, it will raise an `AssertionError` with a clear error message to indicate what specific condition led to the failure.