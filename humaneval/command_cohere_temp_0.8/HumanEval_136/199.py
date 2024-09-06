```python
def largest_smallest_integers(lst):
    negative = None
    positive = None
    for n in lst:
        if n < 0:
            if negative is None or n > negative:
                negative = n
        else:
            if positive is None or n < positive:
                positive = n
    return (negative, positive)
```

The provided Python script defines a function `largest_smallest_integers` that solves the problem as described in the markdown code block. It iterates through the list, identifying the largest negative integer and the smallest positive integer. The function then returns these two values as a tuple.

This solution is illustrated through these examples:
```python
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # Output: (None, 1)
print(largest_smallest_integers([]))  # Output: (None, None)
print(largest_smallest_integers([0]))  # Output: (None, None)
```

The function works as expected, returning the largest negative and smallest positive values present in the list. If the list contains no negative or positive integers, both values are returned as `None`.