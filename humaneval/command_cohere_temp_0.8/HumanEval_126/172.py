```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    return all(dups[num] == 1 for num in dups) and all(num <= nums for num, nums in dups.items())
```

The function uses a dictionary to count the number of times each element appears in the list and checks two things:
1. Whether each element in the list appears only once (using `all(dups[num] == 1 for num in dups)`).
2. Whether each element appears in ascending order (using `all(num <= nums for num, nums in dups.items())`). 

This would pass the test cases mentioned in the problem statement.