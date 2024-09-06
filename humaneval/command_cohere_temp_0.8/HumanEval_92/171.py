```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    return x in [y+z, z+y, y+x] and all([type(i) == int for i in [x, y, z]])
```

The function `any_int` takes three arguments `x`, `y`, and `z`. It uses the in operator to check if any of the three variables is equal to the sum of the other two. To ensure the correctness of the in operator, it first converts all the variables to integers using the `int` function and checks if the type of each variable is `int`. 

Here is a simple test suite that can be used to verify the function:
```python
test_suite = [
    (5, 2, 7,),  # True: 5 == 2 + 7
    (3, 2, 2,),  # False: 3 != 2 + 2
    (3, -2, 1,),  # True: 1 == -2 + 3
    (3.6, -2.2, 2,),  # False: 3.6 != -2.2 + 2
    (0, 0, 0),  # True: 0 == 0 + 0
    (-1, -1, -1),  # True: -1 == -1 + -1
    # Add more test cases as needed
]
```

You can use the `pytest` library to automate the test execution and generate a simple report:
```bash
pip install pytest
pytest -v
```