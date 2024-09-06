```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    return all(dups[num] <= 1 for num in dups) and all(num < nums[1] for num, nums in dups.items())
```

The function uses a dictionary to count the number of times each element appears in the list and verifies two conditions:
1. There are no more than 1 duplicates for each element.
2. The elements are in ascending order.

The function returns `True` if both conditions are met and `False` otherwise. You can use the function by calling `is_sorted()` and passing in the list as an argument. The function will return `True` if the list is sorted with no more than 1 duplicate of any element, and `False` otherwise.