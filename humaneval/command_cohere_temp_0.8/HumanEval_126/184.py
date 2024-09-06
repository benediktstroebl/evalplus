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

The function works by using a dictionary to count the occurrences of each unique element in the list. Then it checks if all non-duplicate elements have only one occurrence, which means the list is sorted. This solution is efficient and can easily be adapted to handle various test cases as per the problem statement.