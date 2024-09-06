Here is a self-contained Python function that solves the problem of returning unique elements from a list:
```python
def unique(lst):
    return list(set(lst))

# Test cases
test_unique = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_unique) == [0, 2, 3, 5, 9, 123]
```
The function unique takes a list as an argument and returns a new list containing only the unique elements from the original list using the set() and list() functions.