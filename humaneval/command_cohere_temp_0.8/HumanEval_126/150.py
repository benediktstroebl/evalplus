```python
def is_sorted(lst):
    lst.sort()
    seen = set()
    for n in lst:
        if n in seen:
            return False
        seen.add(n)
    return True
```

The function first sorts the list, then it iterates through the sorted list, using a set to keep track of seen values. If the list has more than one duplicate entry, the set will have more than one entry for that value, and the function will return false. Otherwise, it returns True. It is worth noting that this solution uses a set to check for duplicates in O(len(S)) time, while other solutions use a dictionary to check in O(num_duplicates * len(S)) time.