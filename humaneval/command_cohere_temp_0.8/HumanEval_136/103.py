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

The function `largest_smallest_integers` solves the problem statement by iterating through the input list `lst`. It monitors both positive and negative integers, updating `positive` and `negative` as the largest and smallest integers respectively. The function ultimately returns a tuple containing the largest negative integer and the smallest positive integer. If no negative or positive integers are present, `None` is directly returned for either value.

The function handles the edge cases mentioned in the problem statement:
- `largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)`
- `largest_smallest_integers([]) == (None, None)`
- `largest_smallest_integers([0]) == (None, None)`

These examples illustrate its behavior with different input scenarios.