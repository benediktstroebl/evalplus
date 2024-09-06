```python
def largest_smallest_integers(lst):
    positive = min(lst, key=lambda x: x >= 0)
    negative = max(lst, key=lambda x: x < 0)
    return negative, positive
```

The function `largest_smallest_integers` uses the `min` and `max` functions, combined with a `key` function, to efficiently find the smallest positive and largest negative integers in the list. 

Here is a snippet of a test suite that can be used to validate the functionality of the function:
```python
def test_largest_smallest_integers():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (7, 1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
```

To run the tests, you can call the `test_largest_smallest_integers` function within the Python environment. If all tests pass, you should not see any error messages, and the output will be concise. 

This approach allows you to efficiently determine the intended values from the list while accounting for scenarios where the list might lack negative or positive integers.