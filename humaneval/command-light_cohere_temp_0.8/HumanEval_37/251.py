```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted."""
    even, odd = lambda i: i % 2 == 0
    l' = [even(i) for i in l] + [odd(i) for i in l]
    return l'
```