```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    Args:
    l (list): list to be sorted
    Returns:
    l' (list): list of integers, with values that are divisible by 3 sorted to the rear, and values that are not divisible by 3 sorted to their original position."""
    l = [1, 2, 3]
    l.sort_by_third(l)
    l = [5, 6, 3, 4, 8, 9, 2]
    l.sort_by_third(l)
    l = [10, 1, 2, 20, 30, 40, 5, 6]
    l.sort_by_third(l)
    l = [100, 200, 300, 400, 50, 60, 7, 8, 9]
    l.sort_by_third(l)
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    l = [50, 60, 30, 20, 10, 8, 7, 9]
    l = [200, 150, 300, 100, 80, 70, 10, 9]
    l = [200, 150, 50, 30, 10, 9]
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return l'
```