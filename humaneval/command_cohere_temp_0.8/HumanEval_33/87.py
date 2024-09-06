```python
def sort_third(l: list):
    l_copy = l.copy()
    return [e if i % 3 != 0 else sorted(l_copy)[i // 3] for i, e in enumerate(l)]
```
This code solves the problem by copying the list l, sorting it, and overwriting the values of the list at indices divisible by three with the sorted values. All other values remain unchanged.