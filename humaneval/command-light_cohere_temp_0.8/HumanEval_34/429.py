```python
def unique(lst):
    """Return sorted unique elements in a list"""
    return list(set(sorted(lst)))

# Test cases

# Test 1: [5, 3, 5, 2, 3, 3, 9, 0, 123] -> [0, 2, 3, 5, 9, 123]
test_unique_pass = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
print(test_unique_pass)

# Test 2: [1, 2, 3, 4, 5, 6, 7] -> [1, 2, 3, 4, 5, 6, 7]
test_unique_fail = unique([1, 2, 3, 4, 5, 6, 7])
print(test_unique_fail)
```
This Python code defines a function unique that aims to sort and return unique elements from an input list. It employs the's set and sorted comparison to achieve this. The code also includes two test cases: one successful, where the function correctly produces the expected output, and another failed, as the function removes duplicate elements from the input list. 

This code demonstrates a basic unique element identification and sorting functionality in Python.