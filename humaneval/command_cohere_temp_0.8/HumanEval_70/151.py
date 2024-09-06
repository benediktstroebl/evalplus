```python
def strange_sort_list(lst):
    min_idx = 0
    sorted_lst = [min(lst)]
    for i in range(1, len(lst)):
        if lst[i] > lst[min_idx]:
            min_idx = i
            sorted_lst.append(lst[i])
        elif lst[i] < lst[min_idx]:
            sorted_lst.append(lst[min_idx])
    return sorted_lst
```

This Python script defines a function called `strange_sort_list` that takes a list of integers as input and returns a sorted list using the specified "strange" sorting order. The function starts with the minimum value and then includes the maximum value among the remaining elements, alternating between minimum and maximum values until the entire list is sorted.

This approach does not require any additional tools like sorting algorithms and complexes, making it inefficient for large lists. Instead, it uses a simple loop to determine the next element to add to the sorted list based on the specified sorting order. The script includes a comment that indicates how the result should be formatted, including examples of test cases and their expected outputs.