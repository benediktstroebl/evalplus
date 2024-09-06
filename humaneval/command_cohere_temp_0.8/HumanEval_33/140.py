```python
def sort_third(l):
    return l[:] if not isinstance(l, list) else [y for i, y in enumerate(l) if i % 3 != 0] + [sorted(x for x in l if i % 3 == 0)]
```

This script defines a function sort_third which takes a list l as an argument and returns a list l’ such that l’ is identical to l in the indices that are not divisible by three, while its values at the indices that are divisible by three are equal to the values of the corresponding indices of l, but sorted. The code works by using list comprehension and the enumerate function to check if the index is not divisible by three, in which case it is kept as it is, or else it is sorted. The latter is achieved using the slice notation to copy the values at the divisible-by-three indices, and the built-in sorted function to sort these values, after which they are appended to the new list. The result is the output of the function.