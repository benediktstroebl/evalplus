```python
def is_sorted(lst):
    lst.sort()
    seen = set()
    for v in lst:
        if v in seen:
            return False
        seen.add(v)
    return True
```

The function first sorts the list, then iterates through the list, using a set `seen` to keep track of the elements encountered while iterating. If the set contains more than one element equal to the current element, the function returns false, else it adds the element to the set and continues iterating. 

The `seen` set is necessary to make the algorithm linear time in the case of duplicate elements, otherwise, the algorithm would be quadratic due to the doubling of elements in each iteration. 

This algorithm guarantees that `is_sorted` will run in O(n log n) time, where n is the length of the input list, making it significantly faster than a naive implementation that checks each element in the list against the previous one.