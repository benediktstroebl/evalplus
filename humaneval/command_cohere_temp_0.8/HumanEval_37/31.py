```python
def sort_even(l):
    even = l[::2]
    odd = l[1::2]
    return even + sorted(odd)
```

The script provides a function `sort_even` that takes a list `l` as an argument and returns a list `l'` such that `l'[i]` is equal to the maximum value of `l[i]` and `l[i]` for all `i` at even indices, and the same value for odd indices as well, but sorted in ascending order.

Here is an example usage of the function:
```python
print(sort_even([1, 7, 3, 4, 2]))  # [1, 3, 2, 4, 7]
```

This would print out the list that is sorted in the specified manner.