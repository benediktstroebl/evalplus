```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return sorted(set(l))

# Test the unique function
test_unique = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
print("Test unique:", test_unique) # [0, 2, 3, 5, 9, 123]

# Test the function multiple times
list_copy = [5, 3, 5, 2, 3, 3, 9, 0, 123]
unique_list = unique(list_copy)
print("Unique list:", unique_list) # Output will be the same as test_unique above
```

The code defines a function named unique that takes a list as input and returns a sorted list of unique elements using the set() function and the sorted() method. The function is then tested using a test list that contains duplicate values and the result is printed. The function is also tested by creating a new list and passing it to the unique function.