```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    return x in [y+z, z+y, x+y] and all(type(i) == int for i in [x, y, z])
```

The function employs a `in` expression to compare the three given numbers `x`, `y`, and `z` with their respective sums, returning `True` if one of them equals the sum of the other two, as specified in the problem. Additionally, it validates if all the elements are integers using the `all` function in combination with a `type` inspection, ensuring the condition is met before returning `True`. 

Here is a test suite to ensure the function behaves as expected:
```python
test_any_int = asyncify(lambda ok, n: n(5, 2, 7) and ok(True), __name__)
test_any_int(lambda ok, n: n(3, 2, 2) and ok(False), lambda ok, n: n(3, -2, 1) and ok(True), lambda ok, n: n(3.6, -2.2, 2) and ok(False))
```

The test suite above uses the `asyncify` function to make sure all test cases are executed sequentially, even though the `test_any_int` function is designed to run test cases concurrently. 

The `test_any_int` function itself takes three arguments: 
- `ok`: a function that performs the assertion, often shortened to `assert` 
- `n`: the function under test (`any_int` in this case) 

The test cases are passed in a lambda function to the `test_any_int` function, which runs them concurrently, asserting the behavior of the `any_int` function in each case. 

To ensure sequential execution for this particular problem statement, please refactor the test suite to execute the lambda functions sequentially against the `any_int` function, like below: 
 ```python
def test_any_int():
    # Initial test cases
    assert any_int(5, 2, 7) == True
    assert any_int(3, 2, 2) == False
    assert any_int(3, -2, 1) == True
    assert any_int(3.6, -2.2, 2) == False

    # Edge cases
    assert any_int(0, 0, 0) == False
    assert any_int(-3, -4, -5) == True

    # Negative tests, where result is False
    assert any_int(-3, -3, -3) == False
    assert any_int(-3, -2, -5) == False
    assert any_int(-3.6, -2.2, 2) == False
```