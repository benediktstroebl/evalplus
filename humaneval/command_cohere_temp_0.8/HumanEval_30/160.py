```python
def get_positive(l: list) -> list:
    """Return only positive numbers in the list."""
    return [x for x in l if x > 0]
```

This Python script defines a function `get_positive` that takes a list `l` as input and returns a list of all positive numbers found in `l`. The function accomplishes this using a list comprehension and filtering logic, ensuring that only elements satisfying the condition `x > 0` are included. 

Here's an example of how you can use the `get_positive` function:
```python
result = get_positive([-1, 2, -4, 5, 6])
print(result)
```

Executing the above code would print out the result `[2, 5, 6]`, which is correct as it returns only the positive numbers from the input list. 

This function is entirely self-contained and can be reused anywhere to filter out positive numbers from any given list. 

If you would like to test this function, you can also incorporate tests like the ones you provided using the `pytest` library like so:
```python
def test_get_positive():
    # Test list with positive and non-positive numbers
    input_list = [-1, 2, -4, 5, 6]
    expected_result = [2, 5, 6]
    result = get_positive(input_list)
    assert result == expected_result

    # Test list with only positive numbers
    input_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    expected_result = [5, 3, 2, 3, 9, 123, 1]
    result = get_positive(input_list)
    assert result == expected_result

test_get_positive()
```

This block of code will run the `get_positive` function against the test cases provided in the docstring and verify that both examples return the expected correct results. 

To run these tests, you can save this code in a Python file (e.g., `test_get_positive.py`) and execute the file using the command `python test_get_positive.py` in your terminal.  Or, if you have `pytest` installed, you can run the tests using the command `pytest test_get_positive.py` which will automatically discover and run the test functions in the file.  This way, you can be confident that the function continues to work as expected with different inputs.