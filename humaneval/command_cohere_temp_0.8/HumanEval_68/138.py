Here's a Python script that solves the given problem with an efficient algorithm using a `dict` to keep track of the nodes with even values:
```python
def pluck(arr):
    even_nodes = {} 
    for i, num in enumerate(arr):
        if num % 2 == 0:
            even_nodes[num] = i
    if even_nodes:
        min_val = min(even_nodes.keys())
        return [min_val, even_nodes[min_val]]
    return []
```

The `dict` approach makes looking up the index for a specific even value O(1) time, which is an improvement over a linear search when there are many even values. The code simplifies by using the `enumerate` feature to directly gather the index while iterating over the list. Finally, the `min` function is optimally used to identify the smallest even value, and its index is directly fetched from the `dict`. The final return value is a list that includes the smallest even value and its corresponding index.