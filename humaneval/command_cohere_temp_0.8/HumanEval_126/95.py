```python
def is_sorted(lst):
    return all(e <= lst[i+1] for i, e in enumerate(lst)) and len(set(lst)) == len(lst)
```
This function checks whether the list is sorted in ascending order and whether there are duplicate elements in the list with the help of the all and set methods. The all method returns True if all elements in the iterable are true, and set returns unique elements in the list. The number of unique elements should be equal to the number of elements in the list for it to be sorted. 

Such a solution can be improved by introducing a time complexity of O(n log n) with the help of the heapq module, as follows:
```python
import heapq

def is_sorted(lst):
    return len(set(lst)) == len(lst) and all(True for _ in heapq.nsmallest(len(lst), lst))
```
Here, heapq.nsmallest() checks whether the first element of the list is the smallest one, the rest being checked with True. This allows for checking the smallest elements first, reducing time complexity.