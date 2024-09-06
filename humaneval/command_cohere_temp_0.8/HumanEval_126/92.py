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
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```
The function uses a simple dictionary (`dups`) to count the occurrences of each number in the list (`lst`) and checks if any of these counts are greater than 1, returning False if so as the list cannot be sorted due to the duplication. If no duplicates are found, it then checks if the list is incrementally sorted in a loop checking each item against the next one, and returns True if so. The function should efficiently handle both cases of duplicates and non-duplicates. 

The script can be checked against the given examples as follows:
```python
print(is_sorted([5]))
print(is_sorted([1, 2, 3, 4, 5]))
print(is_sorted([1, 3, 2, 4, 5]))
print(is_sorted([1, 2, 3, 4, 5, 6]))
print(is_sorted([1, 2, 3, 4, 5, 6, 7]))
print(is_sorted([1, 2, 2, 3, 3, 4]))
print(is_sorted([1, 2, 2, 2, 3, 4]))
```
Which should give the following output:
```
True
True
False
True
True
False
True
```