```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```
This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements from l. The function first removes duplicate elements from the list using the set() function, which removes duplicate values, and then sorts the unique elements using the sort() method. 

Here is an example usage of the function which verifies its correctness:
```python
def test_unique():
    # Test list with duplicates
    l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    assert unique(l) == [0, 2, 3, 5, 9, 123]

    # Test list with no duplicates
    l = [1, 2, 3, 4, 5]
    assert unique(l) == [1, 2, 3, 4, 5]

    # Test empty list
    l = []
    assert unique(l) == []

    # Test list with one element
    l = [7]
    assert unique(l) == [7]
``` 

The test_unique function provides tests for the unique function, checking for correctness in various scenarios including a list with duplicates, a list with no duplicates, an empty list, and a list with one element. 

To run the test, you can use Python's built-in unittest module like this:
```python
import unittest
def test_suite():
    loader = unittest.TestLoader()
    tests = loader.loadTestsFromTestCase(test_unique)
    return tests

runner = unittest.TextTestRunner()
runner.run(test_suite())
``` 

This will run the test_unique function and display the test results, ensuring that the unique function is correct and effective in solving the problem.