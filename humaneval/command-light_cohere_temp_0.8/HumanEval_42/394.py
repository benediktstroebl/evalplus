```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test the function with various inputs
test_incr_list = [1, 2, 3]
test_incr_list_other = [5, 3, 5, 2, 3, 3, 9, 0, 123]

print(incr_list(test_incr_list))  # Output: [2, 3, 4]
print(incr_list(test_incr_list_other))  # Output: [6, 4, 6, 3, 4, 4, 10]
```
The function incr_list is designed to return a new list with a specified number added to each element in the original list. It accomplishes this efficient and concise manner.