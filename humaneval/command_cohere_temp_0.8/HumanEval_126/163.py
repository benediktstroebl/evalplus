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

The function uses a dictionary to count the occurrences of each number in the list and verifies two conditions:
1. There is only one occurrence of each number in the list.
2. The numbers are in ascending order. 

To test the code, you can call the function with various example lists provided in the problem statement.