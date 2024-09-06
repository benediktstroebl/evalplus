```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not == float('inf')]

# Test 1: Should return [] for an empty list
test_case1 = []
result1 = unique(test_case1)
assert result1 == []

# Test 2: Should return [0, 2, 3] for a list [0, 2, 3, 3, 4, 5]
test_case2 = [0, 2, 3, 3, 4, 5]
result2 = unique(test_case2)
assert result2 == [0, 2, 3]

# Test 3: Should return [123] for a list [0, 123, 124]
test_case3 = [0, 123, 124]
result3 = unique(test_case3)
assert result3 == [123]
```
This code defines a function unique that takes a list as input and returns a new list with unique elements from the original list, it uses the set data structure to keep track of elements seen before. The test cases aim to validate the correctness of the unique function by passing various input lists and checking the returned results against the expected output.