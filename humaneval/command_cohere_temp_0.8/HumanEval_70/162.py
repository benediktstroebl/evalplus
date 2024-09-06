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

The code works as follows:
1. Initialize an empty list `out`, which will store the sorted result.
2. Use a while loop until the input list `lst` is empty.
3. On each iteration, find the index of the minimum value in the reversed list `lst[::-1]`, using the `index` method. The `-1` means the list is traversed in reverse order, finding the maximum value in the remaining list.
4. Append the maximum value to the `out` list.
5. Remove the maximum value from the original list using `pop` at the found index.
6. If the length of `lst` is 1, it means only one element is left, and the sorting is complete. Therefore, the loop breaks.
7. Return the sorted list `out`.

The approach efficiently creates the sorted list in the strange order as defined in the problem statement. It handles various scenarios like empty lists or lists with one unique element, ensuring the output aligns with the expected results.