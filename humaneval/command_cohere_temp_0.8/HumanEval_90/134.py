```python
def next_smallest(lst):
    if not lst or len(lst) < 2:
        return None
    mn, mx = min(lst), max(lst)
    sm = mn
    for num in lst:
        if num > mn and num < mx and num != sm:
            sm = num
    return sm if sm != mn else None
```

The function `next_smallest()` employs two basic algorithms:
1. **Non-emptiness Check**: It first checks if the list is empty or has fewer than two elements. In either case, it returns `None` as there is no 2nd smallest value.
2. **Finds the Second Smallest**: 
    - It then identifies the lowest and highest values in the list using the `min()` and `max()` functions, respectively.
    - It initially considers the _minimum_ value as the second smallest, marking it as `sm`.
    - It then iterates through the list, comparing each element:
        - If the element is greater than the minimum _and_ less than the maximum (i.e., it's somewhere in the middle) and isn't equal to `sm`, it updates `sm` to this new value.
    - Finally, the function returns `sm`. However, if `sm` never updates and remains as the minimum, it means there isn't a 2nd smallest value, so it returns `None`.

This algorithm efficiently solves the problem in a straightforward manner.