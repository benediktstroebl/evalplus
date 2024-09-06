```python
def unique(lst):
    return sorted(set(lst))

# Test the function with a sample list
test_unique = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
assert test_unique == [0, 2, 3, 5, 9, 123]

# Another test with list of strings
test_string = unique(["a", "aa", "bb", "ccc", "aaaa", "1", "2"])
assert test_string == ["a", "aa", "bb", "ccc", "aaaa", "1", "2"]
``` 
This function, unique, accepts a list l as input and returns a new list containing only the unique elements of l, which are sorted in ascending order. It is tested using the example list, and also a list of strings.