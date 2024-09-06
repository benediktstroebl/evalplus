```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
This approach employs the Python built-in sorting function `'sort()`'] to arrange the list in ascending order and then retrieves the second last element, which is the second smallest element, from this ordered list. If the list has less than two elements, this method returns None, conforming to the problem's specifications.

Here is a simple test suite for this function:
```python
def test_next_smallest():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([]) == None
    assert next_smallest([1, 1]) == None
```
This test suite verifies the function against the given problem statements. If the function is implemented correctly, all tests should pass.  This would ensure a comprehensive assessment of the function's behavior under various scenarios.