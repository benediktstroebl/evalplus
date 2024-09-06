```python
def sort_even(l):
    even, odd = zip(*[(i, v) for i, v in enumerate(l) if i % 2 == 0])
    return [o if i % 2 else e for i, o, e in zip( enumerate(l), odd, even)]
```

This function takes a list l and returns a list l’ such that l’ is identical to l in the odd indices, while its values at even indices are equal to the values of the even indices of l, but sorted. To achieve this, it uses the zip function to split the list into a tuple of two lists, one of the even indices and one of the odd indices. Following this, a list comprehension is used to replace the even indices in the original list with the sorted version of the even indices derived from the split. The end result is a list l’ where l’[0] = l[0] if l[0] is odd, and l’[0] = sorted(l[0] if l[0] is even, l[2] if l[2] < l[4] if l[4] is not missing, …) if l[0] is even.