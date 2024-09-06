```python
def strange_sort_list(lst):
    out = []
    while lst:
        min_idx = out.append(min(lst))
        lst = [x for i,x in enumerate(lst) if i != min_idx]
    return out
```
The code initiates an empty list out to store the sorted result. It then enters a loop where it keeps track of the index of the minimum value in the remaining list lst. After finding the minimum, it appends it to the 'out' list and removes the minimum value from the list. The loop will continue until the original list is empty and the 'out' list reflects the strange sorted order of the original list. 

The basic logic behind this is to alternate between appending the minimum and maximum value from the remaining list until it is sorted in this strange order. 

The unit tests for this function would look like:
```python
def test_strange_sort_list():
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert strange_sort_list([7, 2, 1, 3]) == [1, 2, 3, 7]
    assert strange_sort_list([10, 10, 3, 1, 2]) == [1, 2, 3, 10, 10]
```