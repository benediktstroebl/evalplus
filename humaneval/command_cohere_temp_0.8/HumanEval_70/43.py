```python
def strange_sort_list(lst):
    out = [min(lst)]
    for x in lst:
        if x > out[-1]:
            out.append(x)
    return out
```

The Python script provides a self-contained function called `strange_sort_list` that takes a list of integers as input and returns a list of those integers sorted in a specific order. This "strange" sort order is unconventional in that it starts with the smallest element, then places the largest remaining element second, then the smallest remaining element third, and so on. The result is that lists with equal elements will retain their order, but the overall order of the elements will be altered.

The function initially builds a starter list to be returned, `out`, by placing the smallest element of the input list first. It then iterates over the remaining elements, comparing each to the last element in `out`. If it finds a larger element, it adds it to `out` immediately after the smallest element. This process continues until all elements have been added to `out` in the unusual but specified order. As a result, the function outputs the provided list sorted in the unusual manner described in the prompt.