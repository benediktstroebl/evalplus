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
    return all(n <= m for n, m in zip(lst, lst[1:]))
```

This Python script defines a function called `is_sorted` that takes a list of numbers as input. It checks whether the list is sorted in ascending order and whether there are any duplicate numbers in the list.

This solution employs a dictionary `dups` to track each element's occurrences in the list. If there's an element occurring more than once, it will be in the dictionary with its key as the element and value as the count. 

It first iterates through the list, updating the dictionary `dups` and checking if any elements appear more than once. If so, it returns `False`, as lists with duplicates aren't considered sorted. Otherwise, it checks if the list is sorted by comparing each element sequentially with the next one. If all comparisons are `True`, the list is sorted, and the function returns `True`.

The script ensures correctness and efficiency in checking the list's sortiness and handles duplicates, making it pass the provided tests.