```python
def strange_sort_list(lst):
    out = []
    while lst:
        min_idx = out.append(min(lst))
        lst = [x for i,x in enumerate(lst) if i != min_idx]
        if len(lst) == 1: break
        max_idx = out.append(max(lst))
        lst = [x for i,x in enumerate(lst) if i != max_idx]
    return out
``` 

The code starts with appending the minimum value from the list (`min(lst)`). Then it removes from the original list all occurrences of this minimum value, leaving the list a bit shorter. If the list became empty as a result, the sorting is finished. Otherwise, the process is repeated: the new maximum value is determined and added to the result, and then it is removed from the list. This way, the result alternates between the minimum and maximum values of what remains in the list after each step.