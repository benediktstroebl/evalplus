```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return list(set(sorted(l)))

# Test the function
test_unique = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
print(test_unique)  # Expected output: [0, 2, 3, 5, 9, 123]
```
This Python function unique takes a list l as input and returns a new list containing only the unique elements from l. The set() function is used to remove duplicates, and the sorted() function is used to sort the elements. The function is then tested using a test case with a sample list and the expected output is printed.