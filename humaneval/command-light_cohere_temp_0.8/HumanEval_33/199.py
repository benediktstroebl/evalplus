```python
def sort_third(lst):
    """Returns a list l' such that l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted."""
    lst = [1, 2, 3]
    return [x for x in lst if x % 3 != 0] + [x for x in lst if x % 3 != 0]
```
I hope this helps!