```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
This Python script sorts the input list and then retrieves the second element (since list indexing is 0-indexed) if the length of the list is at least 2. The function returns `None` if the list has less than two elements, ensuring the correct behavior as per the specified problem and its test cases.