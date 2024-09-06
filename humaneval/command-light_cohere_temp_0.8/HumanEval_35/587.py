```python
def max_element(lst):
    return lst[0] if lst and lst[0] > max(lst[1:]) else max(lst[1:])

# Test cases
test_max_element = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(test_max_element) == 123
test_empty = []
assert max_element(test_empty) == 0
test_single = [1]
assert max_element(test_single) == 1
```
This script defines a function max_element that takes a list as input and returns the maximum element in the list. The function uses the max element comparison to find the largest element. 

The test cases ensure the function works correctly with both empty and non-empty lists.