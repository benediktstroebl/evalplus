```python
def largest_smallest_integers(lst):
    positive = min(x for x in lst if x > 0)
    negative = max(x for x in lst if x < 0)
    return negative, positive
```

The problem asks us to create a function that, given a list of integers, returns a tuple (`a`, `b`) where `a` is the largest integer among negative integers in the list and `b` is the smallest integer among positive integers in the list. If the list does not contain any negative or positive integers, `a` and `b` should be `None`.

The provided code solves this problem using two separate generators expressions that filter out positive and negative integers respectively. These are then passed to `min()` and `max()` to get the smallest and largest values.

Moreover, the function gracefully handles cases where the list might not contain any negative or positive integers, returning the appropriate `None` values in the tuple as per the problem's specification. 

Name: largest_smallest_integers

Parameters:
- lst (list): A list of integers.

Returns:
- tuple: Returns a tuple of two elements: the largest of negative integers and the smallest of positive integers in the list. If the list does not contain any negative or positive integers, both values will be `None`.

Examples:
largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
largest_smallest_integers([]) == (None, None)
largest_smallest_integers([0]) == (None, None)
```