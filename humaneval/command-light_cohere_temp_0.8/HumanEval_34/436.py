```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0]]

# Test 1: Basic functionality
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
# Expected output: [0, 2, 3, 5, 9, 123]

# Test 2: Duplicate values
print(unique([2, 3, 5, 3, 6, 3]))
# Expected output: [2, 3, 5, 6]

# Test 3: List with duplicates and 0
print(unique([0, 2, 3, 5, 3, 7]))
# Expected output: [2, 3, 5, 7]
```
This script defines a function `unique` that takes a list as input and creates a set of unique elements in the list. The function iterates through elements to check if an element is in the seen set and returns it if it's not. If the element is in the seen set, it is added to the result list.