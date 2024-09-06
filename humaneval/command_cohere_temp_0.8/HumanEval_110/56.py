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

The function `exchange()` operates by first locating the indices of even numbers within `lst1` using the list comprehension `even_idxs`. Assuming there are indices of even numbers, the function then proceeds to exchange elements between `lst1` and `lst2` at these indices. Subsequently, the variable `res` is set to 'YES' if the exchange was successful, indicating that all elements in `lst1` are even. In the absence of even numbers in `lst1`, the variable `res` is set to 'NO', indicating that all elements in `lst1` are odd.