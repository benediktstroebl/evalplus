```python
def exchange(lst1, lst2):
    res = 'NO'
    even_idxs = [i for i, x in enumerate(lst1) if x % 2 == 0]
    if len(even_idxs) > 0:
        for idx in even_idxs:
            lst1[idx], lst2[idx] = lst2[idx], lst1[idx]
        res = 'YES'
    return res
```

The approach used in the code is based on swapping elements of both lists using indices of even numbers in `lst1`. The code initially creates a `YES` result if there are even numbers in `lst1` and swaps the elements at even indices with corresponding elements in `lst2`. Finally, it returns the `YES` result if the swapping is successful, otherwise, it returns `NO`.