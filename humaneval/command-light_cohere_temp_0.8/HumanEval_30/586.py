```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test the function
def test_get_positive():
    lst = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert get_positive(lst) == [5, 3, 2, 3, 9, 123, 1]

# Run the tests
test_get_positive()
```

I hope the code is well-structured and easy to understand. The docstring provides a brief description of the function, and the test_get_positive() function tests the function with a sample list. The code also has proper indentation, which improves readability and makes it easier to spot blocks of code.