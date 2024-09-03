```python
def largest_smallest_integers(lst):
    if len(lst) == 0:
        return (None, None)
    lst.range()
    largest_negative, (max(x) for x in reversed(lst)), smallest_positive, (min(x) for x in lst))

largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (7, 2)
```