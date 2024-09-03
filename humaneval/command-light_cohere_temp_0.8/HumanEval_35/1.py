```python
def max_element(lst):
    return lst[-1] if len(lst) == 1 else max(lst)

# Test the max_element function
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

```
This function is a self-contained Python function that solves the problem of finding the maximum element in a list. The function returns the maximum element in the list, if the list has only one element or if the list is empty. The function uses the maximum element from the list as its argument and returns the maximum element.