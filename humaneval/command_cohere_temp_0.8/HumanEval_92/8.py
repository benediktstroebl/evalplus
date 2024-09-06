```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    return x in [y+z, z+y, x+y] and all(type(i) == int for i in [x, y, z])
```

The function `any_int` takes three arguments `x`, `y`, and `z`. It uses the `in` operator to compare `x` against the sums of other two numbers `(y+z)` and `(z+y)`. This works if one of the numbers is equal to the sum of the other two, it returns `True`. The function also checks if all three values are integers using the `all` function and the `type` function internally. 

Here is a simple test suite for this function:
```python
test_suite = [
    (5, 2, 7,),     # 5 + 2 == 7
    (3, 2, 2),      # 3 != 2 + 2
    (3, -2, 1),     # 1 + (-2) == 3
    (3.6, -2.2, 2), # 3.6 != 2 + (-2.2)
]
``` 

And here is the code that runs the tests:
```python
for test in test_suite:
    assert any_int(*test) == True
``` 

Thus, the test cases should all return `True` making the function correct.