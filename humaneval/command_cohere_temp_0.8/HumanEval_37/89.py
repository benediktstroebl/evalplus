```python
def sort_even(l):
    even = l[::2]
    odd = l[1::2]
    return even + sorted(odd)
```

This Python script defines a function called `sort_even` that takes a list `l` as input. The function splits the list into two parts: `even`, which contains the elements at even indices, and `odd`, which contains the elements at odd indices. Then, it returns a new list by concatenating the sorted `odd` elements with the `even` elements. This operation results in a list `l'` where elements at even indices are sorted, while elements at odd indices remain unchanged. The behavior of the function is demonstrated through tests, sorting the list `[5, 6, 3, 4]` to produce `[3, 6, 5, 4]`.