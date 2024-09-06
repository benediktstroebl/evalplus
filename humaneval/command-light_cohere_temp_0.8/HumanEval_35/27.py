```python
def max_element(lst):
    if not_elements(lst):  # Check for empty list
        return None
    return max(lst, default=float('-inf'))

def test_max_element():
    list1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(list1) == 123
    list2 = []
    assert max_element(list2) is None
    list3 = [1, 2, 3]
    assert max_element(list3) == 3
```
This script provides a function `max_element` that calculates the maximum element in a given list. Additionally, it has a corresponding test function `test_max_element` that exercises the `max_element` function with different input lists.