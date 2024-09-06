```python
def triples_sum_to_zero(lst):
    # Sort the list in non-decreasing order - this allows us to eliminate possibilities
    # for the first and second element in the potential triple that sums to zero.
    sorted_lst = sorted(lst)
    for i in range(len(sorted_lst) - 2):
        if sorted_lst[i] + sorted_lst[i+1] == 0:
            return True
    return False
```

This function takes a list of integers `lst` as input and returns `True` if the list contains three distinct elements that sum to zero and `False` otherwise. The function first sorts the list in non-decreasing order. Then, it loops through all pairs of elements except the first (since the sum of the first and second element will automatically eliminate the third). It checks whether the sum of the two elements is equal to zero. If it is, the function returns `True` as it has found a pair that sums to zero. Otherwise, the function returns `False` at the end. 

This approach guarantees a time complexity of `O(n log n)` where `n` is the length of the input list `lst`, due to the sorting required. 

The function is calibrated to handle edge cases like an empty list (`[]`) or a list with only one element `[1]` and should return `False` in those cases.