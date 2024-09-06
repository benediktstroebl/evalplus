```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    for n, v in list(dups.items()):
        if v > 1:
            return False
    return True
```

The function employs a simple algorithm that iterates through each unique number in the list and counts how many times each number appears. The function returns False right away if any number appears more than once, as sorting a list with duplicates is not considered to be sorted. If no duplicates are found, it returns True. 

The algorithm works as follows:
1. Start with an empty dictionary `dups` to hold unique integers from the list and their corresponding counts.
2. Iterate through the list `lst`, for each integer n, do the following:
- Check if n is in the dictionary `dups`.
- If not, add n and set its count to 1.
- If yes, increment its count by 1.
3. After counting duplicates, iterate through the dictionary, if any entry v is greater than 1, return False.
4. If you reach this point, there are no duplicates, so return True.

This solution has a time complexity of O(n), where n is the length of the input list, as it requires a single pass to count the occurrences of each unique element in the list.