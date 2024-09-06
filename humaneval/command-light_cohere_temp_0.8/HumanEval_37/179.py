```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indic of l, but sorted.
    ```
    returns a list [list]
    """
    l = l.copy(reverse=True)
    l[:-2] = [l[1], l[0]]
    return l
```