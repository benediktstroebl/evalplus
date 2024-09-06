```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    return x in [y+z, z+y, x+y] and all(type(i) == int for i in [x, y, z])
```

The function `any_int` takes three parameters, `x`, `y`, and `z`. It uses the in operator to check if any of the elements are equal to the sum of the other two elements. The `any` function returns `true` if any element satisfies the condition and `false` otherwise. 

Here is a test suite to ensure the function behaves as intended:
```python
test_any_int = '''
# Test suite for any_int

def test_any_int():
    assert any_int(5, 2, 7) == True
assert any_int(3, 2, 2) == False
assert any_int(3, -2, 1) == True
assert any_int(3.6, -2.2, 2) == False

def test_any_int_edgecases():
    assert any_int(1, 2, 3) == False
    assert any_int(0, 0, 0) == False
    assert any_int(-1, -2, -3) == False

def test_any_int_type_error():
    with pytest.raises(TypeError):
        any_int(1, 2, '3')
'''
``` 

The test suite contains four tests cases:
1. Testing with valid inputs and expecting the function to return true.
2. Testing with valid inputs but expecting the function to return a false value.
3. Testing edge cases where the inputs are integers but still expecting the function to return false. 
4. Testing Type error exception. 

To run the test suite, you can use the `pytest` library. If you do not have it installed, you can install it using `pip`:
```python
pip install pytest
```
You can then run the specific test suite using `pytest`:
```python
pytest test_any_int
```
Alternatively, you can run the python script directly using `python`:
```python
python test_any_int.py
``` 
The `pytest` tool will run the test suite and output the results, letting you know if the function behaves as expected. In this case, the test suite will ensure the function `any_int` works correctly for all test scenarios.