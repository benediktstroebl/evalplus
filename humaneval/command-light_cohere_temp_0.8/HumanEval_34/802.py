```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x also unique(result))
    return result

# Test cases
test_unique = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_case2 = [4, 6, 7, 8, 9, 10, 2]

# Test results
assert(unique(test_unique) == [0, 2, 3, 5, 9, 123])
assert(unique(test_case2) == [2, 4, 6, 7, 8, 9, 10])
```
This code defines a function called unique that takes a list lst as input and returns a sorted list of unique elements in lst. The function uses a set seen to keep track of elements we've seen before, and a new list result is built by appending elements that aren't in the seen set. The function then returns the unique elements of the list lst.