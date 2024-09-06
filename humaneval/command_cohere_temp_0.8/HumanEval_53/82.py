```python
def add(x: int, y: int):
    """
    Add two numbers x and y
    Returns:
        int: Sum of x and y
    """
    return x + y
```
The function `add()` takes in two integers and returns the sum of the two numbers. The function is self-contained and does not require any external dependencies. 
The tests for this function are straightforward since it's a simple add function. The tests would assert that the function correctly adds two numbers as expected. The `pytest` framework could be used to write the tests efficiently, and the test code would look something like this:
```python
import pytest

@pytest.mark.parametrize("input, expected", [
    (2, 3), (5, 7)
])
def test_add(input, expected):
    result = add(input, input + 1)
    assert result == expected, f"Expected {expected} but got {result}"
```
This piece of code uses the `pytest.mark.parametrize` function to create test cases for the `test_add` function. It passes input and expected output values to `test_add`, which runs the `add` function under test with input and compares the result with the expected output. 
If all tests pass, we can be confident that the `add` function is working correctly.