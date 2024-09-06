```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    for num, count in dups.items():
        if count > 1:
            return False
    return len(set(lst)) == len(lst) and all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```
The function uses a simple dictionary (`dups`) to count the occurrences of each number in the list. If there's more than one occurrence of a number, the list is not considered sorted. After this step, the function returns `False` if there's at least one duplicate in the list, and True otherwise. The function finally returns `True` if there are no duplicates and the list is monotonic increasing. The test cases provided would return:
```
True
True
False
True
True
False
True
```