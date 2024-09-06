```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test cases
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

# This would throw an error if the function wasn't self-contained! 
# Try passing an invalid list, e. at like list or``` also not the list, which is a common error
# in this situation. 
input = [1, 2, -10, -20, 3]
# Attempting to read an invalid member throws an error
# Run into an exception
# cannot be caught in this context. 
# And is why we test with an invalid list. 
```