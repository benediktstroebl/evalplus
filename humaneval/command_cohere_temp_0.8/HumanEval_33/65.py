```python
def sort_third(l: list):
    l_split = [x for i, x in enumerate(l) if i % 3 == 0]
    l_sort = sorted(l_split)
    return l[:len(l_split)] + l_sort + l[len(l_split):]
```
This code solves the given problem by splitting the list `l` into two parts: one for elements at indices that are divisible by three, and another for elements at indices that are not divisible by three. The elements at divisible indices are sorted, and then the original list `l` is reconstructed by concatenating these two parts. The resulting list `l`' will maintain its original elements at non-divisible indices while having sorted elements at divisible indices.