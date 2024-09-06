```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
This approach takes advantage of Python's built-in sorting capability, which allows the list to be sorted in place. Since the list is sorted, the second smallest number is now at the second position. If the length of the list is less than 2, it is returned None, indicating that there is no second smallest number.

Here's the Python testing framework, called pytest, declaring a simple test case that verifies if the `next_smallest` function works as expected:
```python
def test_next_smallest():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([]) is None
    assert next_smallest([1, 1]) is None
```

To run this test, you can use the pytest tool, which is a widely-used, easy-to-use testing framework in Python. After setting up a test file (e.g., naming it `test_next_smallest.py`), you can run the tests by typing `pytest test_next_smallest.py` in your terminal. The output will indicate whether the tests pass or fail.