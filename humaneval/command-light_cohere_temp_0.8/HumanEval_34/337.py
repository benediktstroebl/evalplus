```python
def unique(l: list):
    return sorted([el for el in l if el not in [x for x in l if x == el]])

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result1 = unique(test_case1)
assert result1 == [0, 2, 3, 5, 9, 123], f"Incorrect result: {result1}"

# Test case 2
empty_list = []
result2 = unique(empty_list)
assert result2 == [], "Incorrect result: "

# Test case 3
test_case3 = [5,  3, 9, 1, 2, 7, 8, 3]
result3 = unique(test_case3)
assert result3 == [5, 3, 9, 1, 2, 7, 8], "Incorrect result: "
```

This script defines a function unique that takes a list as input and sorts and returns the unique elements in it. The test cases demonstrate the