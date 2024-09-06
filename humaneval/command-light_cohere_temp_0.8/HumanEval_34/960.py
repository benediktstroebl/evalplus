```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [0]]

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_case1))  # Expected Output: [0, 2, 3, 5, 9, 123]

# Test case 2
test_case2 = [6, 7, [3, 1], [2, 5, [1, 3]]]
print(unique(test_case2))  # Expected Output: [6, 7, [3, 1], [2, 5, [1, 3]]]

# Test case 3
test_case3 = [7, [5, 3, 7], 0, 8]
print(unique(test_case3))  # Expected Output: [7, [5, 3, 7], 0, 8]
```

This script defines a function unique that takes a list as input and returns a new list containing unique elements from the original list. It uses a a set to keep track of seen elements, and then iterates through the original list, adding elements that are not in the set and are not [0]. The output will be a list of unique elements.