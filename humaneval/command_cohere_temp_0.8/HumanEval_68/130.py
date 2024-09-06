Here's a Python script that solves the given problem with an efficient approach using `collections.min` and `filter`:
```python
def pluck(arr):
    # Filter even values and get the minimum node
    even_nodes = filter(lambda x: x % 2 == 0, arr)
    min_even_node = min(even_nodes, key=lambda x: (x, arr.index(x)))
    
    # Return the result as a list
    return [min_even_node, arr.index(min_even_node)]
```

This approach leverages Python's `collections.filter` and `min` functions to efficiently find the smallest even value in the array. The lambda function used in the `filter` is a contentless function intended to test whether a given value is even. The `min` function with the `key` argument allows us to minimize the values based on a custom key function, in this case, the node value and its index in the array.

The resulting list with the minimum even node value and its index is then returned.

Overall, this concise approach elegantly solves the problem in a self-contained and efficient manner.