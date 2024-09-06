```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    Args:
    l (list): list of numbers with potentially odd indexes
    Returns:
    l' (list): list of numbers with odd indexes sorted as described above."""
    l = [3, 2, 1, 6, 4, 8, 5, 9]
    return sorted(l, key=lambda x: x if x % 3 == 1 else x)
```