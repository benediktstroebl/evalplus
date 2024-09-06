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

The function uses a simple dictionary (`dups`) to keep track of how many times each number appears in the list. If there's a duplicate number, it increments the count; otherwise, it initializes the count to 1. After processing all numbers, it checks whether each number has only 1 occurrence (i.e., they are sorted) or not. The `all()` function returns `True` if all conditions are met, and `False` otherwise. 

This solution has an average time complexity of O(n) and a space complexity of O(n) since it requires iterating the list and allocating space for the dictionary. It handles all the edge cases provided in the prompt, including edge cases with an empty list or a list with one number.