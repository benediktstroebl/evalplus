```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test the function
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
```
This code defines the function **get_positive** that takes an input list and returns a new list with only the positive elements from the original list. 

The test_get_positive function passes all the test cases using the **assert** statement, which verifies that the output of the **get_positive** function matches the expected results.