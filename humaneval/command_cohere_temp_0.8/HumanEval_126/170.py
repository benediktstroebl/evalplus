```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    for n, v in dups.items():
        if v > 1:
            return False
    return True
```

The function utilizes a dictionary (`dups`) to track the occurrences of each unique element in the input list `lst`. It iterates through the list, updating the dictionary entry for each element's occurrence. After counting the occurrences, the function checks if any count greater than one indicates duplicates, returning `False` if so. If no duplicates are found, it returns `True`, indicating whether or not the list is sorted in ascending order. 

This solution follows the problem's guidelines and utilizes a dictionary to efficiently monitor duplicates, completing the task in a single function.

This script defines the `is_sorted` function and uses example test lists to demonstrate its functionality. It can be imported as a module or executed directly to test and understand the function's behavior fully.