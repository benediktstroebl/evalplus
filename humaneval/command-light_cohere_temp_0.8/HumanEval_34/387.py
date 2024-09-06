```python
def unique(l: list):
    return list(set(l))

# Test case 1: Should return list with 4 unique elements
test_case1 = [5, 3, 5, 3]
assert unique(test_case1) == [0, 2, 3, 5]

# Test case 2: Should return empty list for empty input list
test_case2 = []
assert unique(test_case2) == []

# Test case 3: Should return list with one unique element
test_case3 = [123]
assert unique(test_case3) == [123]
```
The function unique solves the problem of returning the list of unique elements from the input list. It uses the simple set() and list() methods to achieve this.