```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return list(set(sorted(l)))

# Test cases
 tests = [
    [ [5, 3, 5, 2, 3, 3, 9, 0, 123],
     ['5', '2', '3', '5', '3', '9', '0', 123],
     [5, 3, 5, 2, 3, 3, 9, 0, [123]]
    ]

# Function call
for test_set in tests:
    print(unique(test_set))
``` 
This code defines a Python function named unique that takes a list l as input and returns a new list containing the unique elements of the original list. The function utilizes the unique elements using the set method, which automatically eliminates duplicate elements, and then sorts the remaining elements. Then, the set is converted back to a list using the sorted() function, resulting in a sorted list of unique elements.