```python
def sort_third(l: list):
    l_sorted = [x for i, x in enumerate(l) if i % 3 != 0]
    l_sorted += [sorted(y for y in l if i % 3 == 0)]
    return l_sorted
```
The function `sort_third` takes a list `l` and returns a list `l_sorted` such that `l_sorted` is identical to `l` in the indices that are not divisible by three, while its values at the indices that are divisible by three are equal to the values of the corresponding indices of `l`, but sorted. The list `l_sorted` is returned for use in the main script.