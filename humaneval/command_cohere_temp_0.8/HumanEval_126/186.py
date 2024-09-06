```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    for n, count in dups.items():
        if count > 1:
            return False
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```
The function uses a simple dictionary (`dups`) to count the occurrences of each number in the list (`lst`). If there's a number more than once in `dups`, it returns `False` right away since the list has duplicates and isn't sorted. Otherwise, it proceeds to check if the list is sorted using a Pythonic comprehension and `all()`.