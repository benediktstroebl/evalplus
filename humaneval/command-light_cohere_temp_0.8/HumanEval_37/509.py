```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted.

    >>> sorted([1, 2, 3])
    [1, 2, 3]
    """
    return sorted(l, key=lambda x: not_even(x,l))

def not_even(x,l):
    return x%2==0 and l[x] == l[(x+1)%len(l)]
```

This code defines a `sort_even` function that sorts a list `l` such that the elements at odd positions are sorted as they should be, and the elements at even positions are equal to the elements at corresponding even positions in the original list, but are sorted. The function uses the basic list comprehension, the `not_even` helper function, and the `sorted` function from the Python standard library.