```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```

This Python script provides a function called `next_smallest` that takes a list of integers as input. It sorts the list in ascending order and then checks if the length of the list is less than 2 or not. If the list has less than 2 elements, it returns `None`, indicating that there is no second-smallest element. Otherwise, it returns the second element from the sorted list, which is the second-smallest element in the original list.

Here is a simple test suite for this function:
```python
def test_next_smallest():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([]) == None
    assert next_smallest([1, 1]) == None

test_next_smallest()
```

The `test_next_smallest()` function utilizes Python's `assert` statement to verify that the `next_smallest()` function returns the expected outputs for each test case. 

This is a simple but illustrative example of unit testing in Python. It ensures that the function behaves as expected, aiding in the development of reliable code.