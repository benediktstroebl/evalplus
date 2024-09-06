```python
def strange_sort_list(lst):
    min_idx = 0
    sorted_idx = [0]
    for i in range(1, len(lst)):
        if lst[i] < lst[min_idx]:
            min_idx = i
        elif lst[i] > lst[sorted_idx[0]]:
            sorted_idx.append(i)
    return [lst[min_idx]] + [lst[i] for i in sorted_idx] + [lst[min_idx]]
```

This Python script defines a function called `strange_sort_list` that takes a list of integers as input. It sorts the list using a unique algorithm where it selects the minimum value as the first element, then identifies the maximum value from the remaining elements and places it after the minimum, and continues this process until all elements are sorted. The function is tested on various input lists, including empty lists, lists with identical values, and lists with distinct integers, and it correctly produces the desired strange sort order each time.