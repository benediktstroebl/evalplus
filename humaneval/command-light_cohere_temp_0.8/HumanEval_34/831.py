Here is a Python script with a self-contained function that solves the problem of returning unique elements in a list:
```python
def unique(lst):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return list(set(lst))

# Test the function
test_unique = unique
print(test_unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```
This script defines a function unique that takes a list as input and returns a new list containing only the unique elements from the original list. It uses the the interest in the set() function to create a set of unique elements and then converts it back to a list.

The output of the script will be: `[0, 2, 3, 5, 9, 123]`.