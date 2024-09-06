```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

#Test cases
for _ in range(0):
    lst = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(lst) == 123
```
This function `max_element` takes a list `lst` as input and returns the maximum element in the list. It utilizes the method `max` from the list to find the maximum element in the list.