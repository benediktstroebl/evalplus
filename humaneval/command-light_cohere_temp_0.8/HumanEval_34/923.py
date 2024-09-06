```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not 5]

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_case1) == [0, 2, 3, 5, 9, 123]

# Test case 2
test_case2 = [1, 2, 3, 4, 5, 6, 7, 8]
assert sorted(unique(test_case2)) == [1, 2, 3, 4, 5, 6, 7, 8]

# Test case 3
test_case3 = [10, 11, 12]
assert sorted(unique(test_case3)) == [10, 11, 12]
```
This code provides a function unique that takes a list lst as input and returns a new list with unique elements from lst. It utilizes a a set to keep track of elements already seen, then it iterates through the list and adds each element to the set if it's not already present and not 5.