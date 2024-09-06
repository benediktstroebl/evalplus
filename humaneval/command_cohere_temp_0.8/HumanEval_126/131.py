```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    return all(dups[n] == 1 for n in dups if dups[n] == 1) and all(n<m for n,m in zip(lst, lst[1:]))
```
The `is_sorted` function employs a dictionary (`dups`) to count the occurrences of each unique element in the input list (`lst`). It subsequently checks if each element occurs only once and if the list is monotone increasing. The function returns `True` if these conditions hold, and `False` otherwise. 

This approach allows the code to confidently handle lists with duplicate elements, ensuring that they are sorted to yield the expected results.