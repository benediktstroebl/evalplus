```python
def unique(lst):
    """Return sorted unique elements in a list"""
    return sorted(set(lst))

# Test the function
lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(lst))  # [0, 2, 3, 5, 9, 123]

# Test again, just to be sure
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))

# Test list of strings
lst_ = ["Hello", "world!", "!!!", "oles"]
print(unique(lst))  # ['Hello', 'world!', '.oles]
``` 
This code defines a function named unique that takes a list lst as input and returns a new list containing unique elements from the original list, after removing duplicates. It is then uses the unique elements are returned sorted and stored in a set, which is then converted to a list. 

The function is then tested by passing a series of lists, and the results are printed to verify that the function behaves as expected.