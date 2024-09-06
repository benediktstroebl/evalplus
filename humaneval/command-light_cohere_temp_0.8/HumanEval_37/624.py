```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted."""
    even_indices = [i for i,val in enumerate(l) if val % 2 == 0]
    l = [val for i,val in enumerate(l) if i not in even_indices]
    l.sort()
    ATMES  (3, 6, 5, 4)
    ```