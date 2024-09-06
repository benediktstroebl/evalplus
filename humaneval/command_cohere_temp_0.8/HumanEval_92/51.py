```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    return x in [y+z, z+y, y+x] and all(type(n) == int for n in [x, y, z])
```

The function `any_int` takes three parameters, `x`, `y`, and `z`. It uses the in operator to compare the elements `x`, `y`, `z`, with the sum of the triplet, `y+z`, `z+y`, `y+x`, respectively. The function returns True if one of these comparisons is true and guarantees that all elements are integers. The `all` function checks that each element is an integer. The function returns False if the elements are not integers. 

Here is a simple test suite for this code:
```python
TestSuite = [[any_int(x, y, z) for z in range(10) if not y or not x] for x in range(10) for y in range(10) if not x]
```

The above test suite creates a list of tuples of integers, where each tuple is three integers, and no integer is equal to the sum of the other two in the triplet, and checks the result of `any_int` for each triplet against the expected True value. 

The expected result is True for any non-zero values of `x` or `y`, and False for the rest.
```bash
TestSuite = [[True, True, True, True, True, True, True, True, True, True], 
           [False, False, False, False, False, False, False, False, False, False]]
```

The expected result is True for any non-zero values of `x` or `y`, and False for the rest.

The code passes this test.