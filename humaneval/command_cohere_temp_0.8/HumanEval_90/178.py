```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
This approach takes the list and sorts it with `sorted()`. As a result, the smallest and second-smallest elements are at the first and second positions in the sorted list. So, we extract the second element from the sorted list to get the second-smallest element in the original list. 

We also add a check for the edge case where the list has less than two elements to return `None` in such cases. 

The tests would look like this:
```python
def test_next_smallest():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([]) is None
    assert next_smallest([1, 1]) is None

test_next_smallest()
```

To run the above tests successfully, the correct script needs to be marked as the `test_next_smallest` function.  This way, the tests will be run against the function and show "Passed" as the outcome if the problems are solved correctly.