```python
def strange_sort_list(lst):
    min_idx = 0
    sorted_idx = [0]
    for i in range(1, len(lst)):
        if lst[i] < lst[min_idx]:
            min_idx = i
        elif lst[i] > lst[sorted_idx[0]]:
            sorted_idx[0] = i
    sorted_lst = [lst[min_idx]]
    for i in range(len(sorted_idx)):
        sorted_lst.append(lst[sorted_idx[i]])
    return sorted_lst
```

This Python script defines a function called `strange_sort_list` that takes a list of integers as input. It sorts the list in a strange order, which is like bubble sorting, but it starts with the smallest value, then inserts the largest value among the remaining unsorted values, then the second smallest value, and so on. The function returns the sorted list in this unusual manner.

The algorithm works as follows:
1.  Find the index of the smallest value in the list using the `min_idx` variable and put the smallest value at the beginning of the result list.
2.  Find the index of the largest value in the list among the unsorted elements and insert it after the smallest value in the result list. Update the `sorted_idx` to remove the sorted element.
3.  Repeat steps b. and c. until the list is sorted in this strange manner.