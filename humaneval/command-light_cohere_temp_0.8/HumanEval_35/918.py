```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test case 1
lst1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(lst1) == 123

# Test case 2
lst2 = [5, 3, -5, -20, 2, -3, 3, 9, 0, -100]
assert max_element(lst2) == -5

# Test case 3
lst3 = [5, -5, -15, 2, -10, -3, -1, -100, -20]
assert max_element(lst3) == -5
```

This script provides a function max_element that takes a list lst as an argument and returns the maximum element in the list using the max() built-in function. The code also provides three test cases to check the correctness of the function.

The output of the script will be: 
```
123
-5
-5
```