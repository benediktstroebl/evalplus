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
    return all(n <= m for n, m in zip(lst, lst[1:]))
```

The function employs a dictionary (`dups`) to keep track of the occurrences of each unique element in the input list (`lst`). If any element appears more than once in the list, it will be recorded in the dictionary with its count. 

The function then iterates through the dictionary, and if any element's count exceeds 1, it returns `False` since the condition of having more than one duplicate number is not met. 

Finally, the function uses a list comprehension to check if each element is less than or equal to the next one in the list. If so, the list is considered sorted, and the function returns `True`. 

In summary, the code correctly determines whether the list is sorted while accounting for the constraint of not having more than one duplicate of any element.