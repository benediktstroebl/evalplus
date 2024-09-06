```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not None]

# Test the function with a list of mixed data
assert(unique([5, 3, 5, 2, 3, 'three', 0, 'a']) == [0, 2, 3, 5, 'a']))

# Test with set as input
assert(unique({5, 3, 7, 8, 3, 9}) == [5, 7, 8, 9])

# Test with empty list
assert(unique([]) == [])

# Test with a list of None values
assert(unique([None, 2]) == [None])
```
This code defines a function unique that takes a list as an argument and returns a new list containing only the unique elements from the original list. The function uses a approach of converting the list into a set, and then using the set's notion of uniqueness to filter out the duplicates.

The test cases cover a variety of scenarios, including lists with mixed data, sets, empty lists, and even lists containing `None`.