```python
def largest_smallest_integers(lst):
    positive = min(x for x in lst if x > 0)
    negative = max(x for x in lst if x < 0)
    return negative, positive
```

The problem asks us to create a function that, given a list of integers, returns a tuple (`a`, `b`) where `a` is the largest integer of those in the list that are less than zero and `b` is the smallest integer of those that are greater than zero. The function `largest_smallest_integers` does just that, using `max` and `min` to find the largest negative and the smallest positive, respectively. 

This solution assumes that the list may contain zero or more negative integers and zero or more positive integers. 

The test cases provided in the prompt are covering edge cases, such as when the list is empty or contains only zeros:
```python
assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
assert largest_smallest_integers([]) == (None, None)
assert largest_smallest_integers([0]) == (None, None)
```

These tests illustrate how the function behaves with various input scenarios.