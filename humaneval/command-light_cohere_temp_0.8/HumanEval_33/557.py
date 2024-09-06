```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted. """.
    assert len(l) > 0,
    assert all(i % 3 == 0 for i in l), "All values in the list should be divisible by 3."
    return sorted(l)[::-1]
```