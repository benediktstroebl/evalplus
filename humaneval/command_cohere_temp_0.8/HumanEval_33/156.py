```python
def sort_third(l: list):
    l_copy = l.copy()
    return l_copy[:] [:: (i != len(l) // 3) and (l_copy[i] >= l_copy[i-1] <= l_copy[i+1]) or l_copy[i] for i in range(len(l))]
```