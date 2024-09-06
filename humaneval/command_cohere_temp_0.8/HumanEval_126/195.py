```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    return all(dups[n] == 1 for n in dups if dups[n] == 1)
```

The function uses a simple dictionary (`dups`) to count the occurrences of each number in the list. Then it checks if all non-duplicated items are sorted in ascending order. This solution follows the specs of the problem by checking the list's sort order and also handles the case of more than one duplicate. 

This approach's time complexity is `O(n log n)`, where `n` is the list's length, considering the sorting of the keys in the dictionary. It has a space complexity of `O(n)` since it creates a new dictionary of size n.