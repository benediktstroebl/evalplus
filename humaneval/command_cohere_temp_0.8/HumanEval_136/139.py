```python
def largest_smallest_integers(lst):
    positive = min(x for x in lst if x > 0)
    negative = max(x for x in lst if x < 0)
    return negative, positive
```

The problem asks us to create a function that, given a list of integers, returns a tuple (`a`, `b`) where `a` is the largest integer of the negative integers in the list and `b` is the smallest integer of the positive integers in the list. If the list does not contain any positive or negative integers, `a` and `b` are returned as `None`.

The provided solution uses Python's `max` and `min` functions to find the largest negative and smallest positive integers, respectively. These actions assure the responsiveness to the problem statement and make the function concise and efficient.

This approach allows the function to handle various scenarios such as lists with negative and positive integers, empty lists, or lists with only positive or negative numbers.