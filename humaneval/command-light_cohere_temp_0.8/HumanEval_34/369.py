```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not float('inf')]

# Test 1: Basic Test
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_case1) == [0, 2, 3, 5, 9, 123]

# Test 2: Empty List
test_case2 = []
assert unique(test_case2) == []

# Test 3: List with duplicates
test_case3 = [5, 3, 5, 2, 3, 3, 9, 0]
assert unique(test_case3) == [2, 3, 5, 9]

# Test 4: Float Value
test_case4 = [5.5, 3, float('inf')]
assert unique(test_case4) == [5.5, 3]
```

This script defines a `unique` function that takes a list as input and returns a new list with the unique elements in the original list. The function uses a set to keep track of the elements that have been encountered, and then it iterates through the original list and only adds elements to the set if they are not already in there. This ensures that all elements in the list are unique. 

The test cases provided help to verify the correctness of the `unique` function with various types of input lists.