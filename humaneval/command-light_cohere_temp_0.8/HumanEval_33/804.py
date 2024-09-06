```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.

    Args:
    l (list): list to sort

    Returns:
    l' (list): List where values at indices that are divisible by three are unchanged, and the values at the other indices are sorted.

    Test Cases:
    >>> l = [1, 2, 3]
    >>> sort_third(l)
    [1, 2, 3]
    >>> l = [5, 6, 3, 4, 8, 9, 2]
    >>> sort_third(l)
    [2, 6, 3, 4, 8, 9, 5]
    >>> l = [1, 2, 3, 4, 8, 9, 2]
    >>> sort_third(l)
    [2, 3, 8, 1, 4, 6, 9]
    """
```