```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even index of l, but sorted.
    Input:
    l = [1, 2, 3]
    l.append(4)
    l.sort()
    design_even function
    return a list of the even indices of l, then the
    corresponding elements, and finally, the original list l."""
    return [i for i, x in enumerate(l) if x%2 == 0]
```