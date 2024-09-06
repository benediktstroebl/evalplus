```python
def strange_sort_list(lst):
    result = []
    while lst:
        min_idx = result.index(min(lst)) + 1 if result else 0
        result.append(lst.pop(min_idx))
    return result
```

The code solves the problem using a `while` loop that repeats until the input list `lst` is empty. In each iteration, it finds the minimum value in both the remaining list elements (`min(lst)') and in the previously sorted result (`result`) at the current position, adding the larger of the two to the output and removing it from the input list. The process continues until the input list is depleted, at which point the sorted list is returned as `result`. 

The `index` method finds the position of the minimum value through comparison sorting, while `pop` removes it from the list. Notably, the initial index of the minimum value in the result is determined by `index(min(lst)) + 1`, ensuring that the minimum value is correctly picked in cases where it is not at the start of the input list.