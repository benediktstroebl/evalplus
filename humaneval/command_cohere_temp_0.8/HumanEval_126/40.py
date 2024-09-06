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
    return len(set(lst)) == len(lst) and all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```
The function uses a simple algorithm that takes a list of numbers and checks if it is sorted in ascending order, ignoring duplicate values. The function checks each number to see if it has any duplicates nearby, using a dictionary called `dups` to track each number's occurrences. If any number appears more than once and is not the largest value in the list, the function returns false. Otherwise, it checks the relative order of each value, only returning false if the list has no duplicates and the values are sorted.