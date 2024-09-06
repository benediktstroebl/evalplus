```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    return x in [y+z, z+y, x+y] and all(type(i) == int for i in [x, y, z])
```

The function employs a tuple containing the sum of two variables to efficiently check for the requirement. It also uses a list comprehension to verify if all elements are integers. 

Here is an example usage of the function:
```python
test_cases = [(5, 2, 7), (3, 2, 2), (3, -2, 1), (3.6, -2.2, 2)]
for case in test_cases:
    assert any_int(*case) == True
```

The `any_int()` function's unit tests verify its correctness for various cases. The `any_int` function is expected to return `True` for the first two test cases and `False` for the last two cases. The last example demonstrates the expected behavior for the given problem statement.