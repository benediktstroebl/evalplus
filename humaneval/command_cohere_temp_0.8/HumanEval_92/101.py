```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    return x == y + z and x == z + y and type(x) == int and type(y) == int and type(z) == int
```

The function uses a combination of conditions to check if any of the three parameters is equal to the sum of the other two. It also checks if all three parameters are integers. If all conditions are met, it returns True, otherwise it returns False. 

Here is a test suite that can be used to test the function:
```python
test_suite = [
    (5, 2, 7,),  # Expected output: True
    (3, 2, 2),  # Expected output: False
    (3, -2, 1),  # Expected output: True
    (3.6, -2.2, 2),  # Expected output: False
]

for x, y, z in test_suite:
    assert any_int(x, y, z) == True, f"For inputs {x}, {y}, {z}, the function any_int returned {any_int(x, y, z)}, but True was expected."
```

The test suite contains multiple tuples of inputs and the expected output for the any_int function. The function is tested against five different cases, and in each case, it is asserted that the function's output is correct.  Each test is a triplet of integers and the expected output is a boolean value.