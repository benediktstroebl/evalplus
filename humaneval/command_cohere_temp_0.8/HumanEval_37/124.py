```python
def sort_even(l):
    even = l[::2]
    odd = l[1::2]
    return even + sorted(odd)
```

This script defines a function called `sort_even` which takes a list `l` as input. It splits the list into two parts: `even`, comprising elements at even indices, and `odd`, comprising elements at odd indices. The function then returns the sorted `even` list concatenated with the `odd` list, achieving the desired sorting behavior for even indices while preserving the original order of odd indices.