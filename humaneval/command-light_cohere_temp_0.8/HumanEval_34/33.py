```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0, ]]

# Test case:
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_list) == [0, 2, 3, 5, 9, 123]
```
This code defines a function unique that takes a list lst as input and returns a new list with unique elements from the original list. The function uses a necessary to create a set seen, then iterates over the original list and adds elements to the set if they are not already in it and not the sentinel value []. The test case ensures that the function behaves as expected, returning the correct unique elements from the input list.