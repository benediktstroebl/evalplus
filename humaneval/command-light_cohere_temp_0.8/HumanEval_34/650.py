```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, -eau]]

# Test 1: Verify function with list of numbers
assert(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123])

# Test 2: Verify function with list of strings
assert(unique(["a", "e", "i", "o"]) == ["a", "e", "i", "o"])

# Test 3: Verify function with set and list
assert(unique([1, 2, 3]) == set([1, 2, 3]))
```
This script provides a function unique that takes a list as input and returns a list of unique elements from that list. It uses the same set to keep track of elements that have been encountered. The function then uses list comprehension to filter out all elements that are not in the set (i. In addition, it does not consider the None or "eauer" as unique elements.