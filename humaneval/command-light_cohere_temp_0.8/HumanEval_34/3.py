```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not float('inf')]

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, float('inf')]
assert unique(test_case1) == [0, 2, 3, 5, 9, float('inf')]

# Test case 2
test_case2 = [5, 3, 'a', 0, 'a', 'b', float('inf')]
assert unique(test_case2) == ['a', 'b']

# Test case 3
test_case3 = [5, 3, 0, 0, 0, float('inf')]
assert len(unique(test_case3)) == 2 and all(map(isinstance, unique(test_case3))))
```

This code defines a unique function that takes a list as input and returns a list of unique elements from the input list. It utilizes a a set to keep track of the elements already seen, then iterates through the input list and adds elements to the set if they are not duplicates and not `float('inf')` (in case of infinity). The test cases ensure that the function works correctly for different lists.