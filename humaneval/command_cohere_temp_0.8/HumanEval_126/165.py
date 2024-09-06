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

The function works by first checking if there are any elements in the list that appear more than once. If there are, and their count is more than 1, it returns false as such a list cannot be sorted. Otherwise, it checks if the list is monotonically increasing by checking if the current element is less than or equal to the next one for all consecutive pairs of elements in the list.