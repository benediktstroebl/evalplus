```python
def strange_sort_list(lst):
    result = []
    while lst:
        min_idx = result.index(min(lst)) + 1 if result else 0
        result.append(lst.pop(min_idx))
    return result
```

The code initiates an empty result list before entering a loop over the input list `lst`. Within each iteration, the code identifies the minimum value in the accumulated result so far (`result`) or, if `result` is empty, in the remaining input list. The minimum value's index is determined using `result.index(min(lst))`, considering an offset of 1 if the min value is not in `result`, and this element is appended to `result`. The loop iterates until the input list is empty, thereby producing the desired 'strange' sort order in the `result`. 

The approach utilizes a resultant stack-like structure to retain the minimized values within each iteration and eventually outputs the sorted list in the specified odd manner.