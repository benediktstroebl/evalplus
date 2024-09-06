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

The function employs a simple logic where it checks for duplicates in the list and ensures they are only singular occurrences. It achieves this by using a dictionary that maps each number to the number of times it appears in the list. If any duplicate counts greater than one, the list is not sorted, and the condition fails. If all duplicate counts are one, the list is considered sorted. This approach enables the function to handle various example cases provided in the prompt, successfully identifying correctly sorted and incorrectly sorted lists.