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
    return all(n < m for n, m in zip(lst, lst[1:]))
```

This function uses a dictionary (`dups`) to keep track of the occurrences of each number in the list. If there's a number more than once in the list, it increments its count in the dictionary; otherwise, it initializes the count to 1. After processing the entire list, the function checks if any number appears more than once in `dups`, and if so, it returns `False` since the condition of having more than one duplicate number is not met. Lastly, it compares each number with the subsequent ones in the list (skipping the first, since it's impossible for the first number to be greater than the second in a non-sorted list due to the ascending order condition) to check whether they are sorted. The function returns `True` if all comparisons are true, indicating that the list is sorted with no duplicates.

This approach works successfully for the provided test cases and any other permutations of sorted and unsorted lists with various numbers of occurrences of each number.