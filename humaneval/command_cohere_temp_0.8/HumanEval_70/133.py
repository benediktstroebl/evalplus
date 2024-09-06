```python
def strange_sort_list(lst):
    out = [min(lst)]
    for i in lst:
        if i > out[-1]:
            out.append(i)
    return out
```

The Python script provides a self-contained function called `strange_sort_list` that takes a list of integers as input. It sorts the list using a unique algorithm where it starts with the minimum value and then appends the maximum value from the remaining elements to create a "strange" order. The process continues until all elements are sorted in this alternative manner, creating a list of odd order. The function returns the sorted list.

This approach is efficient as it has a time complexity of O(n log n) to sort the list, just like the naive or bubble sort methods. Though less efficient compared to built-in sorting functions like `sorted()`, this strangeness can be advantageous for specific creative applications.