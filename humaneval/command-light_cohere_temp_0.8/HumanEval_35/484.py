```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

#Test case 1:
test_max_element([1, 2, 3]) #3

#Test case 2:
test_max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) #123

#Test case 3:
test_max_element([5, "abc", -5, 2, -3, 3, 9, 0, 123, 1, -10]) #abc

#Test case 4:
test_max_element([1, 2, -3, 4, 5]) #-3
```