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

The function employs a simple logic to check for duplicates in the list. It uses a dictionary to count the occurrences of each unique element and then checks if all non-unique elements have an occurrence count of 1. You can use this function to solve the problem as per the given test cases. Feel free to ask any questions or make further requests!