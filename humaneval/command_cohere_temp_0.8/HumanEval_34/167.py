```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    l = list(set(l))
    l.sort()
    return l
```
This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements from l. The function uses the built-in set function to remove duplicate elements from the list, and then uses the sort function to sort the unique elements. 

To ensure the function works as expected, let's test it with several cases:
```python
# Test case with repeating elements
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [0, 2, 3, 5, 9, 123]

# Test case with unique elements
print(unique([1, 2, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]

# Test case with empty list
print(unique([]))  # Output: []

# Test case with single element
print(unique([6]))  # Output: [6]
```

This confirms that the `unique` function works correctly for different scenarios. If you have further questions or need assistance with other coding problems, feel free to ask!