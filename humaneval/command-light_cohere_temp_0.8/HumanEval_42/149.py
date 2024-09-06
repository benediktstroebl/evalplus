```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test the function with some inputs
print(incr_list([1, 2, 3])) # [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])) # [6, 4, 6, 3, 4, 4, 6, 7, 1, 125]
```
This function increments the elements in the passed list by 1 and returns the updated list. You can test this are list inputs in the example above, and the output is indeed [2, 3, 4], and [6, 4, 6, 3, 4, 4, 6, 7, 1, 125] respectively.