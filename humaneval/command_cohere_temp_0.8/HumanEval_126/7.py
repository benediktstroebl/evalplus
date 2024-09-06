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

The function uses a simple dictionary (`dups`) to keep track of the occurrences of each number in the list. If there's a number more than once in the list, it will be in the dictionary with a count greater than 1, and the function returns False. If there are no duplicates, it proceeds to check if the list is numerically sorted in ascending order, and returns True if so. The final line handles the case of a list with no duplicates, but the logic can easily be extended to lists with duplicates. 

The `all` function is used in the latter part to check if the list is sorted, as it checks the boolean value returned by each comparison, and short-circuits as soon as a false value is hit, making the code snippet efficient. 

This solution allows for a concise implementation in Python while maintaining the prescribed criteria for the problem.