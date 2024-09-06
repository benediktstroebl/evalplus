```python
def sort_even(l):
    even = l[::2]
    odd = l[1::2]
    return even + sorted(odd)
```

The function `sort_even` takes a list `l` as input and returns a list `l'` that is identical to `l` in the odd indices, while in the even indices it is sorted. The strategy is to create two separate lists, `even` and `odd`, which comprise the even and odd indices of the original list, respectively. We then sort the `odd` list and concatenate it with the `even` list.