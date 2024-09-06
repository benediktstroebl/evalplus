```python
def strange_sort_list(lst):
    out = [min(lst)]
    for i in lst:
        if i > out[-1]:
            out.append(i)
    return out
```

The Python script provides a function called `strange_sort_list` that takes a list of integers as input and returns a list of those integers sorted in a specific order. This "strange" sort order is unconventional in that it starts with the smallest element, then inserts the largest remaining integer, then the smallest, and so on. The goal is to create a list with a mix of smallest-to-largest and largest-to-smallest ordering, creating a strange yet still sorted list.

To achieve this, the function first inserts the smallest element from the input list into the `out` list. Then, it iterates through the remaining elements in the input list, comparing each element to the last value in the `out` list. If the current element is larger than the last element in `out`, it gets appended to `out`. This process continues until all input elements are processed, resulting in a "strangely" sorted list.