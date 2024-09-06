```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    return all(dups[n] == 1 for n in set(dups))
```

This function first counts the duplicates of each number in the list using a dictionary `dups`. If there's a number in `dups` that has a count of more than 1, the function returns False. Otherwise, it returns True. 

The markdown code block for the above code is given below:
```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    return all(dups[n] == 1 for n in set(dups))
```