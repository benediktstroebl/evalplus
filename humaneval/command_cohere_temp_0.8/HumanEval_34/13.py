```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    seen = set()
    return sorted({x for x in l if not (x in seen or seen.add(x))})
```

This approach utilizes a set, `seen`, to keep track of unique elements encountered while iterating through the list `l`. The list comprehension {x for x in l if not (x in seen or seen.add(x))} creates a set of all elements in `l` that are not already in the `seen` set. The `not (x in seen or seen.add(x))` condition effectively checks if the element `x` is not already in the `seen` set, and if not, adds it to the set. The `sorted()` function is then applied to convert the set into a sorted list. 

This approach ensures that each element is considered only once, and the result will be a sorted list of unique elements from the input list. 

The unit tests could involve testing the function on various input lists and confirming that the output list contains only unique elements, and these elements are sorted in ascending order. 
For example:
```python
# Test 1: Basic test case
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Test 2: List with duplicates at the beginning
assert unique([5, 5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Test 3: List with duplicates in the middle
assert unique([0, 5, 3, 5, 2, 3, 5, 9, 123]) == [0, 2, 3, 5, 9, 123]

# Test 4: List with duplicates at the end
assert unique([0, 5, 3, 5, 2, 3, 3, 9, 123, 123]) == [0, 2, 3, 5, 9, 123]

# Test 5: List with duplicates and custom key
assert unique([('a', 1), ('a', 2), ('b', 1), ('c', 3)], key=lambda x: x[1]) == [('a', 1), ('b', 1), ('c', 3)]
```

In these tests, the function is called with different lists of varying duplication patterns, and the assert statements verify that the output list conforms to the expected pattern of unique elements in sorted order. Possibly these tests could be adapted to your specific requirements, such as incorporating additional test cases to account for edge scenarios and handling optional parameters. 
Feel free to modify the tests accordingly, they should help verify that the function behaves as expected for various scenarios.