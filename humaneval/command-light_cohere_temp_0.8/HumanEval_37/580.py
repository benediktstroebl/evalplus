```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal
    to the values of the even index of l, but sorted.

    :param list l: list of integers
    -> l' : list of integers
        """
    even,odd = l[:],l[1:]
    l' = [x if x%2==0 else x+1 for x in l]
    return l'
```