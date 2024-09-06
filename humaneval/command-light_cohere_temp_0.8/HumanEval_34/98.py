Here's a self-contained Python function that returns unique sorted elements in a list:
```python
def unique(lst):
    return sorted(set(lst))

# Test cases 

# Test 1: Unique elements from a list
test1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test1) == [0, 2, 3, 5, 9, 123]

# Test 2: Mixed data with duplicates
test2 = [5, 3, 2, 3, 'abc', 9, 0]
assert unique(test2) == [5, 3, 2, 3, 'abc', 9]

# Test 3: Empty list
test3 = []
assert unique(test3) == []
```
This function uses the `sorted` function along with the `set` function to ensure all elements are unique and then sorted. It uses this same list comprehension to filter out duplicate elements and then sorts the remaining elements.

This function can be easily imported and used in other scripts or projects, promoting reusability and modularity.