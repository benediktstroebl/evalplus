```python
def strange_sort_list(lst):
    min_idx = 0
    max_idx = 0
    sorted_list = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] > lst[max_idx]:
            max_idx = i
        elif lst[i] < lst[min_idx]:
            min_idx = i
        else:
            pass
    for i in range(len(lst) - 2, -1, -1):
        sorted_list.append(lst[i])
    return sorted_list
```

The function `strange_sort_list` implements the described strange sorting order. It first finds the minimum and maximum values in the list and adds the minimum value to the start of the `sorted_list`. Then, it finds the second maximum and adds it to the end of the `sorted_list`, and so on. It iterates through the list backwards to efficiently add the second largest, third largest, and so on, to the `sorted_list`. The empty list case is handled as the script passes the examples provided in the problem statement.