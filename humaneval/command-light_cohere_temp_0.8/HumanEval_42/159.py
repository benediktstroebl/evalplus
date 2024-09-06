```python
def incr_list(lst):
    return [i + 1 for i in lst]

# Test the function with sample inputs
list1 = [1, 2, 3]
assert incr_list(list1) == [2, 3, 4]

list2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert incr_list(list2) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Improper list case - should raise an error
try:
    incr_list([5, 6])
except TypeError as e:
    assert str(e) == "TypeError: 'list' object does not support item assignment"
```
The provided Python function `incr_list` takes a list as an argument and returns a new list with elements incremented by 1. The test cases ensure the can increment the list and handle the case of an improper list, which should raise an error.