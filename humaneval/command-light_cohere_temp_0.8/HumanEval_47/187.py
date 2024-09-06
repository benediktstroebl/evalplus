```python
def median(lst):
    """Return median of elements in the list lst"""
    return (len(lst) % 2 == 0 and median_even(lst) or median_odd(lst))

def median_even(lst):
    """Return median of even elements in the list lst"""
    return sum((x + y) / 2 for x, y in zip(lst, lst[1:])) / len(lst)

def median_odd(lst):
    """Return median of odd elements in the list lst"""
    return sum((x - y) for x, y in zip(lst, lst[1:])) / len(lst)
```

This code defines a function `median` which calculates the median of a list. The `median_even` and `median_odd` functions calculate the median for lists with even and odd last elements, respectively.

This code is a self-contained solution to the problem you have provided.