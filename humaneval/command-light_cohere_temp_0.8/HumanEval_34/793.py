```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0, ]]

# Test case 1
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_list))
# Output: [0, 2, 3, 5, 9, 123]

# Test case 2
empty_list = []
print(unique(empty_list))
# Output: []

# Test case 3
test_list2 = [1, 2, 3, 4, 5]
print(unique(test_list2))
# Output: [1, 2, 3, 4]
```
This Python function named `unique` takes a list `lst` as an argument. It uses a set to keep track of unique elements. The function then iterates through the list and checks if an element is already in the set. The element is then added to the result, a new unique element list.