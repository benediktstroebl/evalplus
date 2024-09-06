```python
def unique(lst):
    return sorted(set(lst))

# Test case using list comprehension for input
test_unique = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = unique(test_unique)
assert set(result) == set([0, 2, 3, 5, 9, 123])
```
This code defines a unique function that returns a sorted set of unique elements in the input list, and then uses this function with a test case to verify its correctness. 
Note that this approach ensures uniqueness by using the set data structure and the sorted() function, which automatically filters out duplicates.  This _ aspects of duplicate elements, and returns a sorted set of unique values.