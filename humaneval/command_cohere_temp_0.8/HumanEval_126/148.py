```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    for n, count in dups.items():
        if count > 1:
            return False
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```
The function uses a simple dictionary (`dups`) to keep track of the duplicates as it iterates over the list. If there are any elements with a count > 1 in `dups`, it returns `False` immediately since duplicates aren't allowed.

After checking for duplicates, it then checks if the remaining unique elements are sorted by iterating through pairs of elements using a generator expression, checking if each element is less than or equal to the next. If this condition is true for all pairs, the function returns `True`. If any pair fails this condition, it returns `False`. Thus, its overall time complexity is O(n^2), where n is the length of the input list.