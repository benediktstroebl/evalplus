```python
def unique(lst):
    """Return sorted unique elements in a list"""
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique(x))
    return result

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_case1) == [0, 2, 3, 5, 9, 123]

# Test case 2
test_case2 = [5, 5, 2, 3, 0]
assert unique(test_case2) == [2, 3]

# Test case 3
test_case3 = [5, 3, 2, 1, 2]
assert unique(test_case3) == [2, 1]
``` 
This Python function named unique solves the problem of finding unique elements in a list. The function uses a set to keep track of the elements it has encountered so far, then iterates through the input list, appending elements to the result list if they are not already present in the set. The function then returns the unique elements of the list.