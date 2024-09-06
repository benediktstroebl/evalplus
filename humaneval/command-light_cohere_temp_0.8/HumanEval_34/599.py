```python
def unique(l: list):
    return list(set(l))

# Test the function with a sample input
test_unique = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_unique) == [0, 2, 3, 5, 9, 123]
```
This script defines a function unique that takes a list as an argument and returns a new list containing only the unique elements from the original list using the set() and list() methods. The test_unique list is used to verify the correctness of the function with a sample input.

The output will be: **[0, 2, 3, 5, 9, 123]**.