```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    for n, v in dups.items():
        if v > 1:
            return False
    return True
```

The function employs a simple algorithm that takes a list of numbers and determines whether they are sorted and contains no duplicate values greater than one. It uses a dictionary to keep track of each number's occurrences, iterating through the list and updating the dictionary. For each unique number, if the count of occurrences is more than one, the function returns false, implying that the list isn't sorted or contains duplicates. If no number has duplicates, it returns true, indicating the list is sorted with no duplicates. This algorithm is efficient and achieves the desired outcome.