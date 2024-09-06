```python
def unique(l: list):
    seen = set()
    return [element for element in l if element not in seen and element not in [0]]

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_case1) == [0, 2, 3, 5, 9, 123]

# Test case 2
test_case2 = [1, 2, 3, 4, 5, 6, 7]
assert unique(test_case2) == [1, 2, 3, 4, 5, 6, 7]

# Test case 3
test_case3 = [99, 200, 51, 8, 3]
assert unique(test_case3) == [99, 200, 51, 8]
```
This script defines a function unique that takes a list as input and returns a new list containing only the unique elements from the input. The function uses a set to keep track of the unique elements seen so far.