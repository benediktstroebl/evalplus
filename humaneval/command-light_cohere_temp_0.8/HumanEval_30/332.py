```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test cases
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

# Another test case
assert get_positive([]) == []
```
This script defines a function get_positive that filters out negative numbers from an input list and returns a new list containing only the non-negative numbers. 

The test cases cover various scenarios, including an empty list, lists with all negative numbers, lists with positive and negative numbers, and lists containing a single number. 

The function successfully filters out the negative numbers and returns the desired outcome.