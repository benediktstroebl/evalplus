```python
def sort_even(l):
    even = l[::2]
    odd = l[1::2]
    return even + sorted(odd)
```

This Python script defines a function called `sort_even` that takes a list called `l` as input. Inside the function, it creates two separate lists: `even` and `odd`. The `even` list contains the values at even indices of the input list, and the `odd` list contains the values at odd indices of the input list. The function then returns the concatenation of the `even` and `sorted(odd)` lists, achieving the desired sorting behavior for even indices while preserving the original order of odd indices.