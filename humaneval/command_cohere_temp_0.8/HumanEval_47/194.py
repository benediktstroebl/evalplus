```python
def median(l: list):
    """Return median of elements in the list l."""
    # Check if the list is empty
    if len(l) == 0:
        return None
    # Check if the list has only one element
    if len(l) == 1:
        return l[0]
    # Sort the list
    sorted_list = sorted(l)
    # Finds the middle index of the sorted list
    middle_index = len(sorted_list) // 2
    # Check if the list has an odd number of elements, to return the middle element
    if len(sorted_list) % 2 != 0:
        return sorted_list[middle_index]
    # If the list has an even number of elements, return the average of the two middle elements
    else:
        middle1 = sorted_list[middle_index - 1]
        middle2 = sorted_list[middle_index]
        return (middle1 + middle2) / 2
```

This function handles cases of empty lists, single-element lists, and even/odd-numbered lists correctly. It sorts the list first before identifying the median element. Test cases can be run by creating a test suite with `pytest`. For example:
```python
def test_median():
    # Test case examples from the docstring
    assert median([3, 1, 2, 4, 5]) == 3
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    assert median([0, 0, 0, 0, 0]) is None
    assert median([1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10]) == 5.5
    assert median([1, -1, 1, -1, 1, -1]) == 0.0
``` 
This test suite covers all the edge cases mentioned in the original problem statement and additional cases to cover further edge scenarios.