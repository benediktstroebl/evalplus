```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements from l. The function uses the built-in `set` function to remove duplicate elements from the list, and then uses the `sort` function to sort the unique elements. 

To ensure the function works as expected, let's test it against a few scenarios:
```python
# Test 1: Basic Test
assert unique([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]

# Test 2: Empty List
assert unique([]) == []

# Test 3: List with Negative Values
assert unique([-3, -2, -1, -1, 1, 2, 3]) == [-3, -2, -1, 1, 2, 3]

# Test 4: List with Floating Point Numbers
assert unique([1.5, 1.75, 2.0, 2.25, 2.5]) == [1.5, 1.75, 2.0, 2.25, 2.5]

# Test 5: Large List
assert unique([1, 2, 3, 4, 3, 1, 5, 6, 7, 8, 9, 8, 7, 6]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

The test cases above cover a wide range of scenarios to ensure that the `unique` function works correctly for various types of input lists.

With these test cases, you can be more confident about the functionality of the `unique` function. If you encounter any further problems or need assistance with other coding challenges, please do not hesitate to ask.