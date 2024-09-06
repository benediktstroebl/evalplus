```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    return all(dups[n] == 1 for n in dups if dups[n] != 1)
```

The function uses a simple dictionary (`dups`) to count the occurrences of each number in the list lst. If there are any elements in `dups` that have a count greater than 1, the list is not considered sorted. The function returns True if the list has no duplicates, and False otherwise. You can test the script by calling the function with different lists to see if it correctly identifies the sorted lists.  This solution has a time complexity of O(n) and a space complexity of O(n).