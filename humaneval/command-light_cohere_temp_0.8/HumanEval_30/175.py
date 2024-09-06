```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test the function with a list containing mixed numbers
test_data = [ -1, 2, -4, 5, 6, 0, -3, 3, 9, -10 ]
assert get_positive(test_data) == [ 2, 5, 6, 0, 3, 9  ]
assert len(get_positive([-5, -20, -100])) == 4

# Test the function with a list of only positive numbers
positive_test = [ 2, 5, 6, 9, 23, 44 ]
assert get_positive(positive_test) == positive_test
assert len(get_positive([88, 99, 33, 88] )) == 4
```
This script defines a function `get_positive` that takes a list l as input and returns a new list containing only the positive elements from l. The test section shows how the dry runs the `get_positive` function with different input lists and verifies the expected results.