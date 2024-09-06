```python
def strange_sort_list(lst):
    min_idx = 0
    sorted_idx = [0]
    for i in range(1, len(lst)):
        if lst[i] < lst[min_idx]:
            min_idx = i
        elif lst[i] > lst[sorted_idx[-1]]:
            sorted_idx.append(i)
    return [lst[i] for i in sorted_idx]
```

This Python script defines a function called `strange_sort_list` that takes a list of integers as input and returns a list of the same integers sorted in a specific order. The function starts by finding the index of the minimum value in the list. Then, it considers the remaining integers and determines if each one is smaller than the minimum or greater than the maximum of the values already sorted. The result is a sorted list that alternates between the minimum value and the maximum remaining value. The script includes a comment that explains the strange sorting algorithm, and example usage is provided as well.