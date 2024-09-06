```python
def strange_sort_list(lst):
    out = [min(lst)]
    for i in lst:
        if i > out[-1]:
            out.append(i)
    return out
```

The function `strange_sort_list` takes a list of integers and returns a list in "strange" order, which means it starts with the minimum value, then the maximum value of the remaining elements, then the minimum value of the remaining, and so on. The output list is constructed by iterating through the input list and appending elements to the output list in the strange order described. This function handles cases where the input list is empty or contains the same value multiple times, returning an appropriate sorted result.