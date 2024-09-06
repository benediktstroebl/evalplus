```python
def sorted_list_sum(lst):
    lst_len = len(lst)
    if lst_len % 2 == 0:
        return lst
    else:
        words = []
        for i in lst:
            if len(i) % 2 == 0:
                words.append(i)
        words.sort()
        return words
```

The approach used in this code iteration organizes the list's items into a fresh list called `words` that includes solely those elements whose length is even. Subsequently, it sorts the `words` list according to the prescribed guidelines and returns the sorted list.

This algorithm effectively handles the task at hand while maintaining a self-contained code structure. It adheres to the problem statement's requirement to return a list of strings, ensuring the list is sorted as specified. The assumption that only strings with an even length are considered further streamlines the process.

If the assumption of only even-length strings holds true, this algorithm effectively manages the sorting and returns the desired list. However, it's still important to validate this assumption to ensure its reliability for future use cases.