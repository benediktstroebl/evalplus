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

The code starts with creating an empty list `out`, to store the sorted result. Then a `while` loop is used to continue until the input list `lst` is empty.

Inside the loop, the code finds the index of the minimum value in the reversed list (`lst[::-1]`) using the `index` method and finding the index of the first occurrence of the minimum value starting from the end of the list `len(lst) - ...`. After that, the minimum value is appended to the `out` list and removed from the original list `lst`.

If the list has only one element, it means that the list is already sorted, and the loop is broken. Finally, the function returns the `out` list which is the sorted list in the specified "strange" order.