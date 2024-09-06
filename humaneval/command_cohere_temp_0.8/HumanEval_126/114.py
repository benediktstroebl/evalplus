```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    return all(dups[n] == 1 for n in dups if dups[n] != 1)
```

The function uses a simple dictionary (`dups`) to keep track of how many times each number appears in the list. If there's a number in the list that appears more than once, the dictionary entry for that number will have a value greater than 1. The function then checks if there's any number in the dictionary with a value of 1, i.e., numbers that appear only once in the list. If there are no such numbers, it returns `True`, meaning the list is sorted with no duplicate values, otherwise it returns `False`. 

This algorithm has a time complexity of O(n) where n is the length of the input list `lst`, as it requires iterating over the list once to populate the dictionary `dups` and once more to check for keys with a value of 1 in the dictionary.