```python
def largest_smallest_integers(lst):
    positive = min(x for x in lst if x > 0)
    negative = max(x for x in lst if x < 0)
    return negative, positive
```

The problem asks us to create a function that, given a list of integers, returns a tuple (`a`, `b`) where `a` is the largest integer of those in the list that are less than zero and `b` is the smallest integer of those in the list that are greater than zero. If the list contains no integers beyond zero or with a magnitude less than zero, `a` and `b` are returned as `None`.

The solution makes use of the `max` and `min` functions, specifically the iterated variants, with Python's comprehension syntax to iterate through the list and find the largest and smallest values respectively. 

Here is the code with some additional tests to ensure it complies with the problem's expectations:
```python
def largest_smallest_integers(lst):
    positive = min(x for x in lst if x > 0)
    negative = max(x for x in lst if x < 0)
    return negative, positive
    
# Tests:
assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
assert largest_smallest_integers([]) == (None, None)
assert largest_smallest_integers([0]) == (None, None)
assert largest_smallest_integers([-1, -2, -3, -4, -99, -111, -222]) == (-222, None)
assert largest_smallest_integers([1, 2, 3, 4, 5, 6, 7, 8, 9]) == (None, 1)
```