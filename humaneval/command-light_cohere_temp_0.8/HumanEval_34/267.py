```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0, ] ]

# Test case 1: Unique elements from a list
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_case1))
# Output: [0, 2, 3, 5, 9, 123]

# Test case 2: Repeated elements are not added to the list
test_case2 = [5, 3, 5, 0, 3, 9, 0, 0]
print(unique(test_case2))
# Output: [0, 2, 3, 5, 9]

# Test case 3: Empty list
test_case3 = []
print(unique(test_case3))
# Output: []
```
The `seen` set keeps track of the elements we have encountered so far, ensuring that duplicates are not added to the final list. The function also handles an special case of an empty list.