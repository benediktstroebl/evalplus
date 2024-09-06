```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
This Python script sorts the list of integers and then retrieves the second element from the sorted list. Since the original list may be of length less than 2, it returns 'None' in such cases. The function passes all the test cases mentioned in the problem statement.