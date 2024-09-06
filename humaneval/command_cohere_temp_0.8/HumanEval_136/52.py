```python
def largest_smallest_integers(lst):
    positive = None
    negative = None
    for n in lst:
        if n > 0:
            if positive is None or n > positive:
                positive = n
        elif n < 0:
            if negative is None or n < negative:
                negative = n
    return (negative, positive)
```

The script defines a Python function `largest_smallest_integers` that solves the problem as described in the markdown code block. It uses `None` to represent the absence of the largest/smallest integer and determines the respective maximum and minimum values among the positive and negative integers in the list. 

This solution assumes that the list may contain zero, none, positive, and negative numbers.

To validate the functionality of the script, you can test it against the examples provided in the problem statement:
```python
assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
assert largest_smallest_integers([]) == (None, None)
assert largest_smallest_integers([0]) == (None, None)
```

Feel free to modify the tests or add more cases to cover a broader range of scenarios.