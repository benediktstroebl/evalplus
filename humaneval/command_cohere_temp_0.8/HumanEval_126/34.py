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
The function `is_sorted` checks for duplicates in the list using a dictionary `dups` to count the occurrences of each unique item. If any item appears more than once in the list, and therefore in `dups`, the function returns False. Otherwise, it proceeds to check if the elements of the list are sorted in ascending order, ignoring duplicates, using a list comprehension and the `all` function. 

The following example usage scenarios from the prompt are showcased:
```python
print(is_sorted([5]))
print(is_sorted([1, 2, 3, 4, 5]))
print(is_sorted([1, 3, 2, 4, 5]))
print(is_sorted([1, 2, 3, 4, 5, 6]))
print(is_sorted([1, 2, 3, 4, 5, 6, 7]))
print(is_sorted([1, 2, 2, 3, 3, 4]))
print(is_sorted([1, 2, 2, 2, 3, 4]))
```
The function passes all these scenarios, returning True for the sorted lists and False for the unsorted ones with duplicates.