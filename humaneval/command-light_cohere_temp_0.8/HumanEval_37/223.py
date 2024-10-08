```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even index of l, but sorted.
    """
>>> sorted_evens([1, 2, 3])
    [1, 3, 2]
    """
    return sorted(l, key=lambda x: x if x % 2 else x // 2)
```