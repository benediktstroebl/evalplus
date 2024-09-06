```python
def strange_sort_list(lst):
    out = []
    while lst:
        min_idx = len(lst) - lst[::-1].index(min(lst))
        out.append(lst.pop(min_idx))
        if len(lst) == 1:
            break
    return out
```

The code initiates an empty `out` list, representing the result after sorting. The program utilizes a `while` loop until the input list is empty. Within each iteration, the minimum value in the list is determined, by using the index of the smallest value flipped backwards through the list. This index is then popped from the list and appended to the `out` list. If the input list contains only a single element, the loop ceases. Finally, the function returns the `out` list, which is the sorted result. 

This algorithm is efficient, with a time complexity of O(n/2) due to the reversed search for the minimum element. 

The code assumes `[]` is a valid input and will return an empty list.  If you do not want to include this edge case, you can modify the empty check `if len(lst) == 1:` to `if len(lst) != 1:`  to exclude the case of an empty list.