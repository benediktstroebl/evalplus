```python
def is_sorted(lst):
    dups = {}
    for x in lst:
        if x in dups:
            dups[x] += 1
        else:
            dups[x] = 1
    for x in dups:
        if dups[x] > 1:
            return False
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```
The function uses a simple dictionary (`dups`) to count the number of duplicates for each element in the list. If there's more than one duplicate for any element, it immediately returns `False` since the list cannot be sorted correctly. Otherwise, it checks if the list is monotonically increasing using the `all()` function and boolean chaining. The `all()` function checks if all conditions are true, and boolean chaining is where you repeatedly apply the AND operator (`&`) to a series of conditions. 

This solution has a time complexity of O(n) and a space complexity of O(n) as it requires iterating the list twice and uses a dictionary to store unique values. It also respects the explicit output format request, providing a function that returns either `True` or `False`.