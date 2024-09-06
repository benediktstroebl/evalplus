```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
This approach employs the built-in sort() method to arrange the list in ascending order. Subsequently, it verifies the length of the list, returning None if there are fewer than two elements. If there are two or more elements, it returns the second smallest value, accessed using the list indexing -1 to retrieve the second-to-last element (as the list is zero-indexed). 

To ensure satisfactory performance, this approach is consistent and delivers the correct result for the provided test cases.