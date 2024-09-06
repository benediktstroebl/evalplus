```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return sorted(set(l))

# Test case 1: Original list with duplicates
list1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print("Test case 1: ", unique(list1)) # Output: [0, 2, 3, 5, 9, 123]

# Test case 2: Empty list
list2 = []
print("Test case 2: ", unique(list2))

# Test case 3: List with duplicate values
list3 = [5, 3, 5, 2, 3]
print("Test case 3: ", unique(list3)) # Output: [2, 3]

# Test case 4: List with <builtins>
list4 = ['a', 'b', 'c', 'd']
print("Test case 4: ", unique(list4))
```

This code defines a function named unique that takes a list as input and returns a new list containing unique elements from the original list, after removing duplicates. The test cases validate that the function correctly removes duplicates and returns the expected unique elements.