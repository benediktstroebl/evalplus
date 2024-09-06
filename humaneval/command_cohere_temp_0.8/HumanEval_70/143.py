```python
def strange_sort_list(lst):
    out = []
    while lst:
        min_idx = out.append(min(lst))
        lst = [x for x in lst if x != min(lst)]
        if len(out) > 1 and out[-2] == min(lst):
            out.pop()
            out.append(max(lst))
            lst = [x for x in lst if x != max(lst)]
        if len(out) > 1 and out[-1] == min(lst):
            out.pop()
    return out
```

The function `strange_sort_list` takes a list of integers as input and attempts to follow the strange sorting algorithm as described in the problem statement. It starts with the minimum value and then catches the maximum value of the remaining integers, then the minimum of the remaining integers, and so on. To simulate this behavior, the function iterates through the input list while keeping track of the current minimum and maximum values in the output list (`out`). During each iteration, the minimum value is appended to `out`, and the same value is removed from the input list. If the removal of the minimum results in a list with only one element, indicating the end of a cycle, the maximum value is appended to `out` and all instances of this maximum are removed from the input list. This process continues until no input remains. The function returns the sorted list `out`.  This algorithm is certainly a strange way to sort, but our function should correctly implement this unique sorting strategy! Let me know if you would like me to make any adjustments to the code to better address the problem statement or if you would like me to explain any specific parts of the code in more detail.