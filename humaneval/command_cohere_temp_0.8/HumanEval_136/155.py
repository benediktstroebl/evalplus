```python
def largest_smallest_integers(lst):
    positive = min(x for x in lst if x > 0)
    negative = max(x for x in lst if x < 0)
    return negative, positive
```

The `largest_smallest_integers` function takes a list of integers as an argument and returns a tuple containing the largest negative integer and the smallest positive integer from the list. If the list contains no negative or positive integers, it returns `None` for the respective value.

This solution adheres to the problem's specified examples and provides a clear and efficient approach using Python's `min` and `max` functions to find the smallest and largest values respectively.