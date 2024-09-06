```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    for num, count in dups.items():
        if count > 1:
            return False
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```
The function uses a simple dictionary (`dups`) to keep track of each unique number and its occurrence in the list. If any number appears more than once in `dups`, the function returns `False` immediately since the list can't be sorted. Otherwise, it checks if the list is increasingly sorted by iterating through all adjacent pairs of elements in the list, inspired by Python's built-in `all` function and the `<=` comparison for simplicity.  This method's time complexity is `O(n^2)`, assuming the list is of integers, but it can be improved to `O(n log n)` with lexicographic sorting if input restrictions are looser.