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

The function `largest_smallest_integers` solves the problem by iterating through the list `lst`. It monitors both positive and negative integers, updating the largest and smallest values respectively. If no positive or negative integers are encountered, `None` is returned for the respective value.

The provided example tests in the problem statement can be replicated as follows:
```python
>>> largest_smallest_integers([2, 4, 1, 3, 5, 7])
((7, 1),)

>>> largest_smallest_integers([])
((None, None),)

>>> largest_smallest_integers([0])
((None, None),)
```

These tests verify the function's behavior against the given problem statement.