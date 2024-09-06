```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l.append(l[n] + 1)
    return l

# Test the function with a sample input list
test_incr_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(test_incr_list)
assert result == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test another sample input list
test_list = [1, 2, 3, 4]
result = incr_list(test_list)
assert result == [2, 3, 5, 4]
```
The code defines a function incr_list that takes a list l as input and returns a new list with elements from input list incremented by 1. 

The test_incr_list is a sample input list that is passed to the incr_list function, and the result is also compared with the expected result using the assert statement. The test_list is another sample input list that is also passed to the incr_list function to test if the function is working correctly.