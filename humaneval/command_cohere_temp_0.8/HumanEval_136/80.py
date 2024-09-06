```python
def largest_smallest_integers(lst):
    positive = min(lst, key=lambda x: x >= 0)
    negative = max(lst, key=lambda x: x < 0)
    return negative, positive
```

The function `largest_smallest_integers` uses `min` and `max` to find the smallest positive and largest negative integers respectively in the list. The `key` argument is used to specify the condition for the values being either negative or positive. 

The function should return `(None, None)` if the list is empty or contains only zero. To ensure this, we add a check for `None` values in the examples before returning the values. 

Here's the full script:
```python
def largest_smallest_integers(lst):
    positive = min(lst, key=lambda x: x >= 0)
    negative = max(lst, key=lambda x: x < 0)
    return None if negative == None or positive == None else (negative, positive)

# Tests
assert(largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1))
assert(largest_smallest_integers([]) == (None, None))
assert(largest_smallest_integers([0]) == (None, None))
assert(largest_smallest_integers([-1, 1]) == (-1, 1))
```

This script can be executed directly to test the function `largest_smallest_integers` with different input lists. Adjust the `assert` statements accordingly if the test cases need to be modified.  If the problem requires additional steps as per the test cases, we can adjust the implementation accordingly, ensuring it passes the given tests.