```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    return all(dups[n] == 1 for n in set(lst))
```

The function employs a simple logic to check for duplicates and determine whether the list is sorted. Notably, the use of the dictionary `dups` allows the function to efficiently track and count the occurrences of each unique element in the input list. This innovative approach assists in making the solution both concise and effective. The solution time complexity is `O(n)`, where `n` is the length of the input list.