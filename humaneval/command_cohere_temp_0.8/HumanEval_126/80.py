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
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```

The function employs a simple algorithm that takes advantage of a dictionary to count the occurrences of each unique element in the list. Then, it iterates through the list and checks if any element appears more than once, returning `False` if so. Finally, it checks if the list is sequentially ordered by verifying that each element is less than or equal to the next one. The script efficiently solves the problem and fulfills the task outlined in the prompt.