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

The function employs two main steps to solve the problem:
1. It uses a dictionary to keep track of the frequency of each number in the list.
2. If there's more than one occurrence of any number, the list is not considered sorted, and the function returns `False`.
3. If there are no duplicate numbers, or if there is only one occurrence of the largest number in the list, the function then checks if the list is sorted by comparing each element with the next one. 

This approach ensures an efficient and accurate check for sorted lists.