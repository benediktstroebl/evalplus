```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    return x in [y+z, z+y, x+y] and all(type(i) == int for i in [x, y, z])
```

The function `any_int` takes three arguments `x`, `y`, and `z`. It uses the `in` operator to compare `x` with the sums of other two numbers (`y` and `z`) and returns `True` if it finds a match and all numbers are integers. The `all` function checks if all conditions are true, in this case, whether all numbers are integers. The `type(i) == int` condition checks if the type of each number is integer. The function returns `False` if the numbers are not integers or the sum is not found. 
Here is a simple test suite to verify the functionality of the function:
```python
TESTS = [
    (5, 2, 7, True),
    (3, 2, 2, False),
    (3, -2, 1, True),
    (3.6, -2.2, 2, False),
    (0, 0, 0, True),
    (-10, -20, 30, True),
    (-2, 2, 4, False),
    (7, 7, 7, False),
    (-3, -7, -1, True)
]

for x, y, z, expected in TESTS:
    print(f"{expected} == any_int({x}, {y}, {z})")
    assert any_int(x, y, z) == expected
```
The test suite contains various test cases to cover different scenarios of input and expected outputs. 
The `assert` statement checks if the output of the `any_int` function equals the expected value for a particular test case. 

The script should be placed in a markdown code block with a title that best describes the purpose of this code, for example:
```
## Problem Solution: any_int Function
```
This way, the title will be aligned with the description of the problem and the code providing a clear context for future reference. 
Feel free to ask if you need anything else!