```python
def unique(lst):
    return list(set(lst))

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_case1) == [0, 2, 3, 5, 9, 123]

# Test case 2
test_case2 = [20, 15, 64, 3, 19]
assert sorted(unique(test_case2)) == [20, 15, 64, 3]

# Test case 3 (Should return empty set on an empty list)
assert unique([]) == []
```
This code defines a unique function that uses the set() function to create a set from a given list. Then, it returns the object the set is an unordered collection of unique objects. The test cases use this test cases with various lists and ensure that the unique function works as expected.