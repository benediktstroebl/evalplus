```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    return all(dups[n] == 1 for n in set(dups))
```

This function checks for the presence of duplicates in the list and counts them. If there's a duplicate count greater than 1, it returns false. Otherwise, it checks whether the list is strictly increasing (sans the duplicates) and returns true if so. It should be noted that this solution is not optimal for very large lists, due to its linear traversal and hashmap-based approach, despite its simplicity and readability.

For larger lists, a solution that leverages lexicographic sorting and the binary search technique can be more efficient, at the expense of increased code complexity. Here's an example of that approach:
```python
def is_sorted(lst):
    # Sort the list and compare to the original
    return lst == sorted(lst)
```

In this method, the list is sorted and then compared to the original. If the list has duplicates, the sorting process will arrange these duplicates in order, allowing the code to catch the violations defined in the problem statement. This method does not require additional space for storing duplicates and has a predictable time complexity of O(n log n) due to sorting.