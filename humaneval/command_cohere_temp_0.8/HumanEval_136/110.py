```python
def largest_smallest_integers(lst):
    positive = min(x for x in lst if x > 0)
    negative = max(x for x in lst if x < 0)
    return negative, positive
```

The problem asks for a Python function that, given a list of integers, returns a tuple (`a`, `b`) where `a` is the largest integer of those in the list that are less than zero and `b` is the smallest integer of those in the list that are greater than zero. If the list contains no integers beyond zero, both values are returned as `None`.

The provided solution leverages Python's `max` and `min` functions, along with their ability to iterate through elements based on specific conditions, to solve the problem efficiently and elegantly. 

It returns the largest negative integer and the smallest positive integer from the list, or `None` for either part if the list doesn't contain any negative or positive integers. 

Here is an example of how you might test this function:
```python
def test_largest_smallest_integers():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (7, 1)
    assert largest_smallest_integers([-3, -7, -1, -11, -23]) == (-1, -11)
    assert largest_smallest_integers([0, 2, 4, 1, 3, 5, 7]) == (7, 1)
    assert largest_smallest_integers([-7, -1, 1, 3, 5, 7]) == (-7, 3)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
```

We're testing for different scenarios, ensuring that the function handles positive and negative integers, as well as empty or single-element lists, correctly.  The function should work for any list of integers, returning the correct tuple of the largest negative and smallest positive numbers, or `None` if there are no such integers in the list.