```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    return all(dups[num] == 1 for num in dups) and all(num < nums[1] for num, nums in dups.items())
```

The function uses a dictionary to count the number of times each element appears in the list and verifies two conditions:
1. Whether each element in the list appears only once (using the dictionary `dups`).
2. Whether each element is less than its subsequent appearance(s) (if any) – this is achieved by iterating the dictionary and comparing each element's first appearance (key) to its subsequent ones (values). 

Both conditions need to be satisfied for the function to return True, otherwise, it returns False.