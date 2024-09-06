```python
def sort_third(l: list):
    l_copy = l.copy()
    return l_copy[:] [::3 == 0] + l_copy[:] [::3 == 1].sort() + l_copy[:] [::3 == 2]
```

The function `sort_third` takes a list `l` and returns a list `l'` that is identical to `l` at indices that are not divisible by three, while the values at indices that are divisible by three are equal to the values of the corresponding indices of `l` but sorted.

The logic behind the above implementation is as follows:
1. First, we make a copy of the original list `l` onto which we will be able to apply mutable operations without affecting the original list. 
2. We then use slicing and boolean indexing to sort the values at the indices divisible by three. The boolean expression `[::3 == 0]` chooses elements at indices that are not divisible by three, `[::3 == 1]` chooses elements at indices that are divisible by three but not equal to 1 (i.e., 3, 6, 9, etc.), and `[::3 == 2]` chooses elements at indices that are divisible by three and equal to 2 (i.e., 6, 12, 18, etc.). Sorting is applied only to the lists corresponding to the second and third conditions.
3. Finally, we concatenate the different slices (or copies) of `l_copy` to form the final list `l'`. 

This implementation ensures that the original list is not modified and uses only elementary operations to create the desired output.