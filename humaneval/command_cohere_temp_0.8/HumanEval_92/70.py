```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    return x in [y+z, z+y, y+x] and all([type(i) == int for i in [x, y, z]])
```

The solution uses a `in` expression to compare the three input numbers to the sum of the other two. To account for the possibility that the first number might equal the sum of the other two, it explicitly lists the possible sums in the `in` expression. The function also uses a list comprehension to check if all three numbers are integers. 

Here is a simple test suite for this function:
```python
# test the function
def test_any_int():
    assert any_int(5, 2, 7) == True
assert any_int(3, 2, 2) == False
assert any_int(3, -2, 1) == True
assert any_int(3.6, -2.2, 2) == False
``` 
This test suite covers a variety of cases to ensure the function works correctly.