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

The function uses a simple dictionary (`dups`) to track occurrences of each number in the list. If there's a duplicate number, it increments the count; otherwise, it initializes the count to 1. Finally, it checks if all counts are 1, except those that are present in the dictionary with a count of 1, implying there are no duplicates. 

This approach enables the solution to succinctly handle various test cases, making it an effective solution to the problem.